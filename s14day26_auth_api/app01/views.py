from django.shortcuts import render,HttpResponse

# Create your views here.

from  django.views import View
import hashlib
import time

class AssetView(View):
    #1.时间  2.是否已经存在   3.正向加密
    def get(self,request,*args,**kwargs):
        visited = []   #列表需要维护时间，如果使用redis或者memcache就简单了
        req_appid = request.META['HTTP_APPID']
        print(req_appid)
        APPID = 'asjdhjasdasgdd'

        v,client_time = req_appid.split('|')
        current_time = time.time()
        float_client_time = float(current_time)
        if current_time - 10 > float_client_time:
            return HttpResponse('验证失败')
        if req_appid in visited:
            return HttpResponse('验证失败')
        m = hashlib.md5()
        m.update(bytes(APPID+client_time,encoding='utf-8'))
        new_appid = m.hexdigest()
        if new_appid == v:
            visited.append(req_appid)
            return HttpResponse('...')
        else:
            return HttpResponse('去你的吧。。。')