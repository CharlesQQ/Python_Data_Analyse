#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import inspect

def out(f):
    def foo(*args,**kwargs):
        print inspect.getcallargs(f,*args,**kwargs).get('kwargs').get('name')
        print args
        print kwargs
    return foo


@out
def test(*args,**kwargs):
    pass
test('aa','bb',name='charles',age=23)