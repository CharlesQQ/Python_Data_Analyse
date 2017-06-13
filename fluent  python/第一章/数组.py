#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

from array import array
from random import random

"""
存放1000万个浮点数，数组的效率比列表高的多
"""
def write():
    """
    tofile写入文件
    :return:
    """
    floats = array('d',(random() for i in range(10**7)))
    fp = open('floats.bin','wb')
    floats.tofile(fp)
    print(floats[-1])
    fp.close()

def read():
    """
    fromfile读取文件
    :return:
    """
    float2 = array('d')    #创建一个数组，只能存放一个字节大小的整数
    fp = open('floats.bin','rb')
    float2.fromfile(fp,10**7)
    fp.close()
    print(float2[-1])
read()

