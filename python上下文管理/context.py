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
        self.msecs = self.secs * 1000
        if self.verbose:
            print "cost time:%s ms" %self.msecs

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) +fib(n-2)

with MyTimer(True):
    print fib(30)