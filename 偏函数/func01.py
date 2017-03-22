#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
# def int8(x,base=8):
#     return int(x,base=base)
#
# print int8('12345')

import functools
int8 =functools.partial(int,base=8)
print int8('12345')