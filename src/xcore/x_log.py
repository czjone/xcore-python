import io
import os
import sys


class x_log():
    def __init__(self):
        pass

    @staticmethod
    def IsWin32()->bool:
        return sys.platform == "win32"

    @staticmethod
    def Error(strdata)->None:
        if not x_log.IsWin32():
            print('\033[0;46;0m [ ERROR   ] ' + str(strdata) + '\033[0m')
        else:
            print('[ ERROR   ] ' + str(strdata))
        raise Exception(strdata)

    @staticmethod
    def Warring(strdata)->None:
        if not x_log.IsWin32():
            print('\033[0;46;0m [ WARRING ] ' + str(strdata) + '\033[0m')
        else:
            print('[ WARRING ] ' + str(strdata))

    @staticmethod
    def Ignore(strdata)->None:
        if not x_log.IsWin32():
            print('\033[0;46;0m [ IGNORE  ] ' + str(strdata) + '\033[0m')
        else:
            print('[ IGNORE  ] ' + str(strdata))

    @staticmethod
    def Info(strdata)->None: 
        if not x_log.IsWin32():
            print('\033[0;46;0m [ INFO    ] ' + str(strdata) + '\033[0m')
        else:
            print('[ INFO    ] ' + str(strdata))

    @staticmethod
    def Ok(strdata)->None:
        if not x_log.IsWin32():
            print('\033[0;47;0m [ SUCCESS ] ' + str(strdata) + '\033[0m')
        else:
            print('[ SUCCESS ] ' + str(strdata))

    @staticmethod
    def Assets(exp,message)->None:
        if not exp:
            raise Exception(message)

    @staticmethod
    def OutVersion():
        x_log.Info(sys.version)
