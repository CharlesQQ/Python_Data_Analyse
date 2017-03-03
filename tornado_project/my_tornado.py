#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define('port',default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        greeting = self.get_argument('greeting',"Hello")
        oldman = self.get_argument('edu','virgin')

        self.write(greeting+oldman+',friendly user!')

    def head(self, *args, **kwargs):   #设置请求头(head请求)，有需要重写:
                                        #请求种类:get post put delete head options
        self.set_status(200)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)])    #注册一个app
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


"""
[root@linux-node1 ~]# curl http://192.168.1.105:8000
Hellovirgin,friendly user![root@linux-node1 ~]#

[root@linux-node1 ~]# curl -I http://192.168.1.105:8000
HTTP/1.1 200 OK
Date: Fri, 03 Mar 2017 14:46:14 GMT
Content-Length: 0
Etag: "da39a3ee5e6b4b0d3255bfef95601890afd80709"
Content-Type: text/html; charset=UTF-8
Server: TornadoServer/4.4.2
"""