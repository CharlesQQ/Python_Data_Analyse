from django.shortcuts import render

# Create your views here.

import requests

def req(request):
    response = requests.get('http://php.weather.sina.com.cn/xml.php?city=%B1%B1%BE%A9&password=DJOYnieT8234jlsK&day=0')
    # print(response.content)   #字节
    response.encoding = 'utf-8'
    # print(response.text)       #字符串
    return render(request,'req.html',{'result':response.text})

    #浏览器具有同源策略，在不接受不同域的数据（阻止ajax请求，无法阻止<script src="..."></script>）
    #解决办法:
        # - 创建script标签
        # - src=远程地址,远程地址返回的数据可以拿到,返回的数据必须符合js格式;