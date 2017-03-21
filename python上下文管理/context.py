#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

class MyContext(object):
    def __init__(self):
        print "__init__"
    def __enter__(self):
        print "open file"
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "close file"

    def func(self):
        print "execute"
context1 = MyContext()

with MyContext():
    print "<hello>"
    MyContext().func()


import time
class MyTimer(object):
    def __init__(self,verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs
        if self.verbose:
            print "cost time:%s ms" %self.msecs

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) +fib(n-2)

with MyTimer(True):
    print fib(30)




print "<--------------------->"
def w1(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        cost = end - start
        print cost,"####"
        print func.func_name    #获取被调用函数的名称
    return inner

@w1
def fib1(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) +fib(n-2)
fib1(30)