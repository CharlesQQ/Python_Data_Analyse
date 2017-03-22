#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

class Foo():
    def __init__(self):
        print "__init__ method"

    def public_method(self):
        print "public_method"

    def __private_method(self):
        print "__private_method"

    def _halfprivate_method(self):
        print "_halfprivate_method"

# f = Foo()
# f._Foo__private_method()
#
#
# class A(object):
#     def __init__(self):
#         self.__private()
#         self.public()
#
#     def __private(self):
#         print 'A.__private()'
#
#     def public(self):
#         print 'A.public()'
#
#     def test(self):
#         raise NotImplementedError
#
# class B(A):
#     def __private(self):
#         print 'B.__private()'
#
#     def public(self):
#         print 'B.public()'
#
#     def test(self):
#         print "the method come true"
#
# b = B()
# b.test()

def _bar():
    print "This is bar"


