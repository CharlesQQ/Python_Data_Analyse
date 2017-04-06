#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class C(object):
    # def __str__(self):
    #     return "test"

    def __repr__(self):
        return "test1"

class B:
    pass


c=C()
print c
print dir(C)
print dir(B)


class A(object):

    @staticmethod
    def foo():
        pass

    def bar(self):
        pass

a=A()
print a.foo
print A.foo
print a.bar
print A.bar


class D(object):
    @classmethod
    def foo(cls):
        print 'class name is',cls.__name__

    @classmethod
    def bar(mycls):
        print 'class name is',mycls.__name__
    name='charles'

d=D()
print d.foo
print d.bar
print D.foo
print D.bar
d.foo()
D.foo()
d.bar()
D.bar()
print d.__dict__

class E(object):
    def __init__(self):
        self.x=1
        self.y=2

    __slots__= 'x','y'

e=E()
print dir(e)
e.x=2


class listNoAppend(list):
    def __getattribute__(self, name):
        if name == 'append':
            raise AttributeError,name
        return list.__getattribute__(self,name)

aa=listNoAppend()
print (aa)