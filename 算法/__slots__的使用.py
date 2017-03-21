#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class Student(object):
    __slots__=('name','age')
    gender='female'
    # name='china'
    # pass

s = Student()
s.name = 'Charles'
s.age=20
print s.name
print s.age
# s.gender='male'

