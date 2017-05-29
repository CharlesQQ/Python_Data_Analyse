#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

import json
from django.shortcuts import render,HttpResponse

from django.forms import fields
from django.forms import widgets
from django.forms import forms


class LoginForm(forms.Form):
    username = fields.CharField()
    password = fields.CharField(
        max_length=64,
        min_length=12,
    )


from django.core.exceptions import ValidationError
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,ValidationError):
            return {'code':o.code,'messages':o.messages}
        else:
            return json.JSONEncoder.default(self,o)

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == "POST":
        ret = {'status':True,'error':None,'data':None}
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(type(obj.errors))   # <class'django.forms.utils.ErrorDict'>
            #from django.forms.utils import ErrorDict

            print(obj.errors.as_json())
            """
            Object {data: null, error: "{"password": [{"message": "Ensure this value has                            a…characters (it has 10).", "code": "min_length"}]}", status: true}
            data
            :
            null
            error
            :
            "{"password": [{"message": "Ensure this value has at least 12 characters (it has 10).",               "code": "min_length"}]}"
            status
            :
            true
            __proto__
            :
            Object
            """
            print(type(obj.errors.as_data()))
            for k,v in obj.errors.as_data().items():
                print(k,v)
            #ret['error'] = obj.errors.as_json()   #在前端需要loads两次
            ret['error'] = obj.errors.as_data()
        result = json.dumps(ret,cls=JsonCustomEncoder)
        return HttpResponse(json.dumps(result))