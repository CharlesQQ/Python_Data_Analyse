#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


class Count(object):
    def add(self,x,y,*arg):
        x+=y
        for val in arg:
            x+=val
        return x

    def sub(self,x,y,*args):
        x-=y
        for val in args:
            x-=val
        return x