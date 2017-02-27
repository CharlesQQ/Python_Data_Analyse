#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
def grains():
    local = {}
    test = {'key':'value','key1':'value1','key2':'value2'}
    local['list'] =[1,2,3,4]
    local['string']='str'
    local['dict'] =test
    return local