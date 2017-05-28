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
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == "POST":
        ret = {'status':True,'error':None,'data':None}
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(type(obj.errors))   #from django.forms.utils import ErrorDict
            print(obj.errors.as_json())
            print(obj.errors.as_data())
            ret['error'] = obj.errors.as_json()
        return HttpResponse(json.dumps(ret))