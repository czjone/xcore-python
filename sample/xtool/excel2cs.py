from x_pipeline import *
from x_log import *
from x_csv import *
class  excel2cs(x_pipeline):

    _csv:x_csv

    def __init__(self,conf) -> None:
        pass

    #override pipeline.GetPipelineName
    def GetPipelineName(self)->None:
        return "Excel2CSharp"

    #override pipeline.OnProcess
    def OnBefor(self)->bool:
        x_log.Info("检查配置文件的正确性")
        return True

    #override pipeline.OnProcess
    def OnProcess(self)->bool:
        x_log.Info("生成配置文件")
        return True

    #override pipeline.OnAfter
    def OnAfter(self)->bool:
        x_log.Info("检查生成文件的正确性")
        return True