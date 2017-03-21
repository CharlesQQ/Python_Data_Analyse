#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class Node():
    __slots__=['_item','_next']    #限定Node实例的属性
    def __init__(self,item):
        self._item=item
        self._next=None     #Node的指针部分默认指向None
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item=newitem
    def setNext(self,newnext):
        self._next=newnext
