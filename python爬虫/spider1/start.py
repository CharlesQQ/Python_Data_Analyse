#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import commands
status,result =commands.getstatusoutput('scrapy crawl s2 --nolog')
print result