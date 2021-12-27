# -*- coding: UTF-8 -*-
import sys
import io
import os
import shutil


class x_file:

    @staticmethod
    def DeleteDir(path:str):
        if os.path.exists(path) == True: 
            shutil.rmtree(path)
    @staticmethod
    def Write(path: str, val: str) -> bool:
        try:
            dir = os.path.dirname(path)
            if os.path.exists(dir) == False:
                os.makedirs(dir)
            fp = open(path, encoding= "utf-8",mode = "w+")
            ret = fp.write(val)
            fp.close()
            return ret == len(val)
        except IOError as err:
            return False

    @staticmethod
    def Read(path: str) -> str:
        try:
            fp = open(path, encoding= "utf-8",mode = "r")
            ret = fp.read()
            fp.close()
            return ret

        except IOError as err:
            return ""

    @staticmethod
    def ReName(inPath: str, destPath: str) -> None:
        try:
            os.rename(inPath, destPath)
        except IOError as err:
            return None

    def GetFiles(inDir:str,pattern:any)->list:
        list_ret = os.listdir(inDir)  # 列出文件夹下所有的目录与文件
        for patten in pattern:
            if len(pattern) > 5:
                raise "Matching rule length must be less than 5."
        #只处理0~4字条的扩展名
        filter_func = lambda path:(path[-1:] in pattern) or (path[-2:] in pattern) or (path[-3:] in pattern) or (path[-4:] in pattern) or (path[-5:] in pattern)
        # filter_func = lambda path:True
        return list(filter(filter_func,list_ret))
        