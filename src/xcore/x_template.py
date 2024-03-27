from abc import abstractmethod
from x_file import *
from x_log import *

class x_template:
    _template:str = None
    _fields = []
    _data = []
    def __init__(self,template:str) -> None:
        self._template = template
        pass

    def ToString(self)->str:
        return self._template

    def SaveTo(self,path:str) ->bool:
        return len(path) != x_file.Write(path,self._template)

    def Replace(self,label:str,val:str) -> bool:
        self._template = self._template.replace(label,val)
        return True

    def SetNamespace(self,namespace:str)->bool:
        return self.Replace('$NS$',namespace)

    def SetClassName(self,className:str)->bool:
        return self.Replace('$CLASS_NAME$',className)

    def SetFirstField(self,field:any)->bool:
        self.SetField(field);
        return self.Replace('$FIRST_FIELDS_TYPE$',field["type"])
    
    def SetFields(self,fields:any) ->bool:
        self.SetFirstField(fields[0])
        self._fields =  fields
        self.ApplyFiled();
        return True;
        
    def SetData(self,data:any) ->bool:
        self._data =  data
        self.ApplyConfigData();
        return True; 

    @abstractmethod
    def SetField(self,field:any)->bool:
        return True

    @abstractmethod
    def AddData(self,data:any) ->bool:
        return True;

    @abstractmethod
    def ApplyFiled(self) ->bool:
        return True;

    @abstractmethod
    def ApplyConfigData(self) ->bool:
        return True;

    @staticmethod
    def create(language:str,template:str):
        if language.lower() == "cs":
            return x_csharp_template(template);
        elif language.lower() == "json":
            return x_json_template(template);
        elif language.lower() == "lua":
            return x_lua_template(template);
        elif language.lower() == "cpp":
            return x_cpp_template(template);
        
        x_log.Error("not supports templates:{}".format(language));
        

class x_csharp_template(x_template):
    def __init__(self, template: str) -> None:
        super().__init__(template)
    
    #override x_template.SetField
    def SetField(self,field:any)->bool:
        return True

    #override x_template.AddData
    def AddData(self,data:any) ->bool:
        return True;
        
    #override x_template.ApplyFiled
    def ApplyFiled(self) ->bool:
        fields = self._fields
        ret = ""
        t = "\t\t\t"
        ret = ret + t + "\r\n";

        # 生成字段
        for field in fields:
            # ret = ret + t + "/// <summary> {} </summary>\n".format(field["des"]);
            ret = ret + t + "public {} {} {} get; set; {} \n".format(field["type"],field["name"],"{","}");
        return self.Replace('$FIELDS$',ret)

    #override x_template.ApplyConfigData
    def ApplyConfigData(self) ->bool:
        itemsArray = self._data
        fields = self._fields
        ret = ""
        t = "\t\t\t"
        firstType = None;
        for itemArray in itemsArray:
            initFieldCode = ""
            for item in itemArray:
                for field in fields:
                    if field['column_letter'] == item['column_letter'] :
                        if 'ignore' in field and "cs" in field['ignore']: continue;
                        if firstType == None:
                            firstType=field["type"]
                        type=field["type"]
                        initFieldCode =  initFieldCode + "{} = {},".format(field['name'],self.GetValue(type, item['val']));
            ret =  ret + "{}{},new Item(){} {} {}{},\n".format("{",self.GetValue(fields[0]["type"],itemArray[0]["val"]),"{",initFieldCode,"}","}") + t
            self.Replace('$CONF_DATA_LIST_FIRST_TYPE$',firstType);
        return self.Replace('$CONF_DATA_LIST$',ret)

    def GetValue(self,type:str,val:any)->any:
        if type == "Int32":
            return int(val);
        elif type == "String":
            if val != None:
                return '"' + str(val) + '"'
            else:
                return "null"
        else:
            return None

class x_json_template(x_template):
    def __init__(self, template: str) -> None:
        super().__init__(template)

    
    #override x_template.SetField
    def SetField(self,field:any)->bool:
        return True

    #override x_template.AddData
    def AddData(self,data:any) ->bool:
        return True;

    #override x_template.ApplyFiled
    def ApplyFiled(self) ->bool:
        # fields = self._fields
        # ret = ""
        # t = "\t\t\t"
        # ret = ret + t + "\r\n";

        # # 生成字段
        # for field in fields:
        #     ret = ret + t + "/// <summary> {} </summary>\r\n".format(field["des"]);
        #     ret = ret + t + "public {} {} {} get; set; {} \r\n".format(field["type"],field["name"],"{","}");
        # return self.Replace('$FIELDS$',ret)
        return True

    #override x_template.ApplyConfigData
    def ApplyConfigData(self) ->bool:
        itemsArray = self._data
        fields = self._fields
        ret = ""
        t = "\t"
        for itemArray in itemsArray:
            initFieldCode = ""
            for item in itemArray:
                for field in fields:
                    if field['column_letter'] == item['column_letter'] :
                        if 'ignore' in field and "lua" in field['ignore']: continue;
                        type=field["type"]
                        if self.GetValue(type, item['val']) == None: continue;
                            
                        initFieldCode =  initFieldCode + '"{}" : {},'.format(field['name'],self.GetValue(type, item['val']));
            initFieldCode = initFieldCode[0:-1]#去掉最后一个逗号
                
            ret =  ret + "{} {} {},\n".format("{",initFieldCode,"}") + t
        return self.Replace('$CONF_DATA_LIST$',ret[0:-3]) #去掉最后一个逗号

    def GetValue(self,type:str,val:any)->any:
        if type == "Int32":
            return int(val)
        elif type == "String":
            if val != None:
                return '"' + str(val) + '"'
            else:
                return "null"
        else:
            return None

class x_lua_template(x_template):
    def __init__(self, template: str) -> None:
        super().__init__(template)
    
    #override x_template.SetField
    def SetField(self,field:any)->bool:
        return True

    #override x_template.AddData
    def AddData(self,data:any) ->bool:
        return True;

    #override x_template.ApplyFiled
    def ApplyFiled(self) ->bool:
        # fields = self._fields
        # ret = ""
        # t = "\t\t\t"
        # ret = ret + t + "\r\n";

        # # 生成字段
        # for field in fields:
        #     ret = ret + t + "/// <summary> {} </summary>\r\n".format(field["des"]);
        #     ret = ret + t + "public {} {} {} get; set; {} \r\n".format(field["type"],field["name"],"{","}");
        # return self.Replace('$FIELDS$',ret)
        return True

    #override x_template.ApplyConfigData
    def ApplyConfigData(self) ->bool:
        itemsArray = self._data
        fields = self._fields
        ret = ""
        t = "\t"
        for itemArray in itemsArray:
            initFieldCode = ""
            for item in itemArray:
                for field in fields:
                    if field['column_letter'] == item['column_letter'] :
                        if 'ignore' in field and "lua" in field['ignore']: continue;
                        type=field["type"]
                        initFieldCode =  initFieldCode + '{} = {},'.format(field['name'],self.GetValue(type, item['val']));
            initFieldCode = initFieldCode[0:-1]#去掉最后一个逗号
                
            ret =  ret + "[{}] = {} {} {},\r\n".format(self.GetValue(fields[0]["type"],itemArray[0]["val"]),"{",initFieldCode,"}") + t
        return self.Replace('$CONF_DATA_LIST$',ret[0:-4]) #去掉最后一个逗号

    def GetValue(self,type:str,val:any)->any:
        if type == "Int32":
            return int(val);
        elif type == "String":
            if val != None:
                return '"' + str(val) + '"'
            else:
                return "null"
        else:
            return None

class x_cpp_template(x_template):
    def __init__(self, template: str) -> None:
        super().__init__(template)

    #override x_template.SetField
    def SetField(self,field:any)->bool:
        return True

    #override x_template.AddData
    def AddData(self,data:any) ->bool:
        return True;

    #override x_template.ApplyFiled
    def ApplyFiled(self) ->bool:
        return True;

    #override x_template.ApplyConfigData
    def ApplyConfigData(self) ->bool:
        return True;
