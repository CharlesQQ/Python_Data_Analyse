#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import time,sched

s = sched.scheduler(time.time,time.sleep)


def event_func1():
    print "func1 Time:",time.time()

def perform1(inc):
    s.enter(inc,0,perform1,(inc,))
    event_func1()

def event_func2():
    print "func2 Time:",time.time()

def perform2(inc):
    s.enter(inc,0,perform2,(inc,))
    event_func2()

def main(func,inc=2):
    if func == '1':
        s.enter(0,0,perform1,(10,))
    if func == '2':
        s.enter(0,0,perform2,(20,))

if __name__ == '__main__':
    main('1')
    main('2')
    s.run()