# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod
from typing import Any
from xcore.x_log import x_log
from xcore.x_utf8 import x_utf8
import sys
sys.path.append("..")

class pipeline:
    
    _conf = None

    def __init__(self, conf):
        self._conf = conf
        pass

    @abstractmethod
    def GetPipelineName(self)->None:
        return "UnDefine pipeline(base pipeline)."

    @abstractmethod
    def OnBefor(self)->bool:
        return False

    @abstractmethod
    def OnProcess(self)->bool:
        return True

    @abstractmethod
    def OnAfter(self)->bool:
        return False

    @property
    def Configure(self)->any:
        return self._conf;
        