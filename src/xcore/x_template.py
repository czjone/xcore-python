from x_file import *

class x_template:
    _template:str = None
    def __init__(self,template:str) -> None:
        self._template = template
        pass

    def ToString(self)->str:
        return self._template

    def SaveTo(self,path:str) ->bool:
        return len(path) != x_file.Write(path,self._template)