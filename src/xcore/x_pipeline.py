# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod
from typing import Any
from x_log import *
from x_utf8 import *
import sys
sys.path.append("..")

class x_pipeline:
    
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
        