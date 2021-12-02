# -*- coding: UTF-8 -*-
import sys
import io
import os


class x_file:

    @staticmethod
    def Write(path: str, val: str) -> bool:
        try:
            fp = open(path, "w+")
            ret = fp.write(val)
            fp.close()
            return ret == len(val)

        except IOError as err:
            return False

    @staticmethod
    def Read(path: str) -> str:
        try:
            fp = open(path, "r")
            ret = fp.read()
            fp.close()
            return ret

        except IOError as err:
            return ""

    @staticmethod
    def ReName(inpath: str, destPath: str) -> None:
        try:
            os.rename(inpath, destPath)
        except IOError as err:
            return None
