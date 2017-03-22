#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class Student(object):
    __slots__=('name','age')
    gender='female'
    # name='china'
    # age = 30

s = Student()
s1=Student()
s.name = 'Charles'
s.age=20
print s.gender
print s.name

# print s1.name
print s.age
# s.gender='male'

class PrimaryStudent(Student):
    __slots__ = ('gender')
s2 = PrimaryStudent()
s2.name = 'eric'
s2.gender='male'
s2.grade=80
print s2.name
print s2.gender

