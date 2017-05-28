#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

from celery import Celery

app=Celery("tasks",
           broker='redis://192.168.74.20',
           backend='redis://192.168.74.20')

@app.task
def add(x,y):
    print "running...",x,y
    return x+y
