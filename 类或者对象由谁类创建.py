#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

# class Foo(object):
#     pass
#
# obj = Foo()
# print type(obj)
# print type(Foo)
#
# class MyClass(type):
#     pass

class MyType(type):

    def __init__(self, what, bases=None, dict=None):
        print "333"
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print "444"
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj)

class Foo(object):

    __metaclass__ = MyType

    def __init__(self):
        print '222'

    def __new__(cls, *args, **kwargs):
        print '1111'
        return object.__new__(cls, *args, **kwargs)

obj = Foo()

class B(object):
    pass
class A(B):
    def __init__(self):
        print self,'----'
        print 'init'

    def __new__(cls, *args, **kwargs):
        print "first"
        return object.__new__(B,*args,**kwargs)
A()