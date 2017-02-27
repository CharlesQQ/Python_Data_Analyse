#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import salt.client
caller = salt.client.Caller()
# print caller.cmd('test.ping')
print caller.function('test.ping')

