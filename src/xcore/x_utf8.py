# -*- coding: UTF-8 -*-
import sys
import io
import os

# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe9 in position 0: ordinal not in range(128)

# 只在python 2的情况下能使用
# reload(sys)
# sys.setdefaultencoding('utf-8')


class x_utf8:
    def __init__(self):
        pass