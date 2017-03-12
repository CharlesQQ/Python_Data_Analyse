#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'



import tornado.ioloop
import tornado.web
class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login1.html')

    def post(self, *args, **kwargs):
        dic = {'status':True,"message":""}
        print(self.get_argument('username'))
        user = (self.get_argument('username'))
        print(self.get_argument('password'))
        pwd = (self.get_argument('password'))
        if user == 'alex' and pwd =='123':
            pass
        else:
            dic['status'] = False
            dic['message'] = "用户名或者密码错误"
        import json
        self.write(json.dumps(dic))


settings = {
    "template_path": "views",  # 模版路径的配置
    "static_path":'static',          #静态文件配置

}

# 路由映射，路由系统
application = tornado.web.Application([  # 创建对象
    (r"/login", LoginHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)  # 创建socket，一直循环
    tornado.ioloop.IOLoop.instance().start()  # 使用epoll,io多路复用