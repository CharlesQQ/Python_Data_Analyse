#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

import importlib

aa = importlib.import_module('lib.aa')
print(type(aa))
print(aa.C().name)

assert isinstance(aa.C().name,str)
print('succ')