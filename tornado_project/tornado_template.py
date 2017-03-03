#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

from tornado.options import define,options
import os
import json
define('port',default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        fjson = open('test.json','r')
        json_data = json.loads(fjson.read())
        fjson.close()
        self.render("index.html",bankenddata=json_data)

if __name__ == '__main__':
    SETTINGS=dict(
        template_path = os.path.join(os.path.dirname(__file__),"templates"),
        static_path = os.path.join(os.path.dirname(__file__),"static")
    )
    urls = [
        (r"/",IndexHandler),
    ]
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=urls,
        **SETTINGS
    )    #注册一个app
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()