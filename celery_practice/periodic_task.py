#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

from celery import Celery
from celery.schedules import crontab

app=Celery()

@app.on_after_configure.connect
def setup_preiodic_tasks(sender,**kwargs):
    sender.add_periodic_task(10.0,test.s('hello'),name='add every 10')

    sender.add_periodic_task(30.0,test.s('world'),expires=10)

    sender.add_periodic_task(
        crontab(hour=7,minute=30,day_of_week=1),
        test.s("Happy Mondays!"),
    )

@app.task
def test(args):
    print args
