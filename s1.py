#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

import requests
appid = 'asjdhjasdasgdd'

import hashlib
import time
current_time = str(time.time())
m = hashlib.md5()
m.update(bytes(appid+current_time,encoding='utf-8'))
new_appid = m.hexdigest()

new_new_appid = "%s|%s" %(new_appid,current_time)
print(new_new_appid)


response = requests.get(
     url='http://127.0.0.1:8080/asset/',
     # params={'appid',appid},
     headers = {'appid':new_new_appid}
 )
print(response.text)