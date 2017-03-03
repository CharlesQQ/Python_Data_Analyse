#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import torndb
db = torndb.Connection(host="192.168.74.20",database="jumpserver",user="root",password="")
a = db.get('select * from auth_permission WHERE id=1')
print(a)

b = db.query('select * from auth_permission')
print(b)

"""
get:只能返回一行数据,是字典格式
query:返回的是列表格式的数据,返回多条;列表的每个元素是字段
"""