#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'



import tornado.ioloop
import tornado.web
class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        pass


settings = {
    "template_path": "views",  # 模版路径的配置
    # "static_path":'statics',          #静态文件配置

}

# 路由映射，路由系统
application = tornado.web.Application([  # 创建对象
    (r"/login", LoginHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)  # 创建socket，一直循环
    tornado.ioloop.IOLoop.instance().start()  # 使用epoll,io多路复用