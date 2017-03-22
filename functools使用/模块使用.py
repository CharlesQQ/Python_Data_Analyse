#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
from functools import cmp_to_key

def compare(ele1,ele2):
    return ele2 -ele1
a = [2,3,1]
print max(a,key=cmp_to_key(compare))



with open('aa',"r") as f:
    pass
