
# from xtool.excel2cs import excel2cs
import sys
from distutils.sysconfig import *
from x_runner import *
from x_log import *
from x_json import *
from excel2code import *

# TODO:用参数的方式控制生成方式

class xTool(x_runner):
    def __init__(self,conf) -> None:
        self.Register(excel2code(conf["Excel2Code"]))
        pass

    @staticmethod
    def GetPythonLibPath()->str:
        return get_python_lib()

if __name__ == "__main__":
    conf = x_json.LoadFromFile("config.json")
    # x_log.Info(conf);
    # ret = xTool.GetPythonLibPath()
    # # x_log.Info(ret)
    xtool:xTool = xTool(conf)
    xtool.Run()