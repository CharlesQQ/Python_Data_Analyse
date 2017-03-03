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


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        self.get_secure_cookie("username",self.get_argument("username"))
        self.redirect("/")

class WebcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('welcome.html',username=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("username")
        self.redirect("/")

if __name__ == '__main__':
    SETTINGS={
        "template_path" :os.path.join(os.path.dirname(__file__),"templates"),
        "static_path": os.path.join(os.path.dirname(__file__),"static"),
        "cookie_secret":"ddsddsdsdsds",
        "login_url":"/login"          #如果用户没有获取到cookie的话,就会重定向到login这个url

    }
    urls = [
        (r"/",WebcomeHandler),    #没有cookie，自动登录到login页面
        (r"/login",LoginHandler),
        (r'/test',WebcomeHandler),
        (r'/loout',LogoutHandler),
    ]
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=urls,
        **SETTINGS
    )    #注册一个app
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()