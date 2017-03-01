#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'',views.welcome),
    url(r'moment_input',views.moment_input),
]