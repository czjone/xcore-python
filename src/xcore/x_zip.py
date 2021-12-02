# -*- coding: UTF-8 -*-
from x_log import x_log
from x_utf8 import x_utf8
from openpyxl import load_workbook
import os
import sys
import zipfile

from xcore.x_log import x_log


class x_zip:

    def __init__(self):
        super().__init__()

    @staticmethod
    def UnzipSingle(srcfile: str, destfile: str, password: str = ""):
        ''' 解压单个文件到目标文件夹。
        '''
        if password:
            password = password.encode()
        zf = zipfile.ZipFile(srcfile)
        # x_log.Info(srcfile)
        try:
            zf.extractall(path=destfile, pwd=password)
        except RuntimeError as e:
            print(e)
            pass

        zf.close()

    # @staticmethod
    # def UnzipAll(srcdir: str, destdir: str, password: str = ""):
    #     if not os.path.isdir(srcdir):    # 如果是单一文件
    #         x_zip.UnzipSingle(srcdir, destdir, password)
    #     else:
    #         it = os.scandir(srcdir)
    #         for entry in it:
    #             if entry.is_file() and os.path.splitext(entry.name)[1] == '.zip':

    #                 x_zip.UnzipSingle(entry.path, destdir +
    #                                   "/" + apkname, password)
    #             else:
    #                 # x_log.Ignore("not suports file:" + entry.name)
    #                 pass

    @staticmethod
    def UnzipAllApks(srcdir: str, destdir: str) -> bool:
        if not os.path.isdir(srcdir):
            x_log.Error("input directory path is file:" + srcdir)
            return False
        else:
            it = os.scandir(srcdir)
            for entry in it:
                if entry.is_file() and (os.path.splitext(entry.name)[1] in ['.apk', '.xapk']):
                    apkname = os.path.splitext(entry.name)[0]
                    # apkext = os.path.splitext(entry.name)[1]
                    x_zip.UnzipSingle(entry.path, destdir + "/" + apkname, "")
                    x_log.Ok("unzip:" + entry.name)