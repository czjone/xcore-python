import os
from x_csv import *
from x_pipeline import *
from x_log import *
from x_file import *
from x_template import *

class  excel2code(x_pipeline):

    _InDir:str = None
    _Excels:any= []
    _FieldsConf = None
    def __init__(self,conf) -> None:
        super().__init__(conf)
        self._FieldsConf =  conf["Excel"];
        pass

    #override pipeline.GetPipelineName
    def GetPipelineName(self)->None:
        return "Excel2CSharp"

    #override pipeline.OnProcess
    def OnBefor(self)->bool:
        self._InDir = self.Configure["InDir"]
        files = x_file.GetFiles(self._InDir,".xlsx")
        for i in range(0, len(files)):
            path = os.path.join(self._InDir, files[i])
            if os.path.isfile(path):
                csv = x_csv(path)
                self._Excels.append(csv)
        return True

    #override pipeline.OnProcess
    def OnProcess(self)->bool:
        language = self.Configure["Language"].split('|');
        outDir = self.Configure["OutDir"]
        ns = self.Configure["Namespace"]
        x_file.DeleteDir(outDir);
        for l in language: #生成不同语言的配置
            #加载模板
            templatestr:str = x_file.Read('xtool/templates/{}.template'.format(l.lower()))
            for csv in self._Excels:
                csv.Load()
                x_log.Info("==== 处理:"+csv.Path)
                names = csv.SheetNames
                for name in names:
                    #生成代码
                    sheetconf = self.GetSheetFieldConf(name)
                    if(sheetconf!= None):
                        outFileName = sheetconf["out"] + "." + l
                        outfile = os.path.join(outDir, l + "/" + outFileName)
                        #模板替换
                        template:x_template = x_csharp_template.create(l,templatestr);
                        template.SetNamespace(ns);
                        template.SetClassName(sheetconf["out"]);
                        #设置字段类型
                        template.SetFields(self.GetTemplateFields(sheetconf["field"],csv,name))
                        #解析数据
                        data = []
                        csv.EachRows(name,lambda index,ret: self.HandleRow(index,data,ret))
                        template.SetData(data);
                        #保存代码 
                        if True == template.SaveTo(outfile):
                            x_log.Ok(outFileName + " <= " + name);
                        else:
                            x_log.Error(outfile + " <= " + name);
        return True
    
    def GetTemplateFields(self,fields:any,csv:x_csv,sheetname:str):
        rowIndex = 1
        f = []
        for dic in fields:
            for k,v in dic.items():
                kSplit = k.split(':');
                headName = csv.GetRowValueWith(sheetname,str(kSplit[1])+str(rowIndex)).strip('0');
                confName = kSplit[0 ].strip('0');
                #检查表头设置是否正确 比如A1 的值是否与配置档相同
                x_log.Check(headName,confName , "配置档错误:'{}' <= '{}' {}".format (confName , headName,k))
                #设置字段
                vSplit = v.split(':');
                field = {}
                field["name"] =  vSplit[0]
                field["type"] =  vSplit[1]
                field["des"] =  kSplit[0]
                field["column_letter"] =  kSplit[1]
                if len(vSplit)==3 and vSplit[2]!= "":
                    field["ignore"] = vSplit[2].lower().split("|")
                f.append(field);
        return f;

    def HandleRow(self,rowIndex:int, retData:any,data:any)->None:
        if rowIndex <=1:
            return;
        ret = []
        for d in data:
            ret.append({"column_letter":d.column_letter,"val" : d.value});
        retData.append(ret)
        pass

    #override pipeline.OnAfter
    def OnAfter(self)->bool:
        x_log.Info("检查生成文件的正确性")
        return True

    def GetSheetFieldConf(self,sheetName:str)->any:
        if sheetName in self._FieldsConf:
            return self._FieldsConf[sheetName]