# -*- coding: UTF-8 -*-
from x_utf8 import *
from x_log import *
from x_file import *
import json


class x_json:

    @staticmethod
    def LoadFromFile(jsonpath: str) -> any:

        jsontext: str = x_file.Read(jsonpath)
        if(jsontext == ""):
            x_log.Error("json file is empty:" + jsonpath)
            return None

        return x_json.LoadFromString(jsontext)

    @staticmethod
    def LoadFromString(jsontext: str) -> any:
        return json.loads(jsontext)

    @staticmethod
    def ToJsonString(data: any) -> str:
        return json.dumps(data)

    @staticmethod
    def SaveToJson(jpath: str, data: any) -> str:
        with open(jpath, 'w', encoding='utf-8') as fObj:
            json.dump(data, fObj, ensure_ascii=False)