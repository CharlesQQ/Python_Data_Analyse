#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

#引入python wsgi包
from wsgiref.simple_server import make_server

#服务端程序代码

def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<b>Hello,world!</b>'

server = make_server('',8080,application)
server.serve_forever()