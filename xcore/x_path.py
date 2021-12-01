# -*- coding: UTF-8 -*-
import sys
import io
import os


class x_path:

    @staticmethod
    def _get_script_in_dir_path() -> str:
        return sys.path[0]
        # return os.getcwd();

    @staticmethod
    def GetMainScriptPath() -> str:
        return x_path._get_script_in_dir_path()