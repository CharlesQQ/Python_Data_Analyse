#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from django.shortcuts import render,HttpResponse
from django.forms import fields as Ffield
# from django.forms import forms
from django import forms
from django.forms import widgets as Fwidgets

from  app01 import models


class UserInfoModelForm(forms.ModelForm):

    is_rmb = Ffield.CharField(        #自定义额外的字段,可以实现一个月内免登录的功能(不需要写数据库)
        widget=Fwidgets.CheckboxInput())

    class Meta:
        model = models.UserInfo1    #记住:每一行末尾都不要加逗号
        fields = '__all__'
        # fields = ['username','email']
        # exclude = []
        labels = {
            'email':'邮箱',
        }
        help_texts = {
            'username':'....',
        }
        widgets = {
            'username':Fwidgets.Textarea(attrs={'class':'c1'})
        }
        error_messages = {
            '__all__':{         #整体的错误信息

            },
            'email':{
                'required':"邮箱不能为空",
                'invalid':"邮箱格式不对",
            }
        }

        fields_classes = {
            # 'email':Ffield.URLField
        }
        # localized_fields = ('ctime')   #哪些字段做本地化

    def clean_username(self):    #钩子和form相同
        old = self.cleaned_data['username']
        return old

class UserInfo1Form(forms.Form):
    username = Ffield.CharField(max_length=32)
    email = Ffield.EmailField()
    user_type = Ffield.ChoiceField(
        choices=models.UserType1.objects.values_list('id','caption')
    )

def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request,'index1.html',{'obj':obj})
    elif request.method == 'POST':
        # obj = UserInfo1Form(request.POST)
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            # obj.save()   #直接保存到数据库中,包括的多对多的,就不需要后续的操作了
            instance = obj.save(commit=False)   #下面这三个操作步骤和obj.save()的效果相同，instance.save()不会保存多对多的数据,obj.save_m2m()会将多对多的数据保存进数据库
            instance.save()
            obj.save_m2m()
        print(obj.is_valid())
        print(obj.cleaned_data)
        print(obj.errors.as_json)
        return render(request,'index1.html',{'obj':obj})

#Form验证
# UserInfoForm-->Form-->base form
# UserInfoModelForm-->Form-->base form

def user_list(request):
    obj = models.UserInfo1.objects.all().select_related('user_type')   #select_related不能使用多对多
    return render(request,'user_list.html',{'li':obj})

def user_edit(request,nid):
    #获取当前用户id对应的用户信息
    #显示用户已经存在的数据
    if request.method == 'GET':
        user_obj = models.UserInfo1.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request,'user_edit.html',{'mf':mf,'nid':nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo1.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST,
                               instance=user_obj)  # 如果是更新操作，使用instance指定哪些对象的数据需要被更新，如果不加instance参数，默认就是增加数据
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_json)
        return render(request,'user_edit.html',{'mf':mf,'nid':nid})

def ajax(request):
    return render(request,'ajax.html')

def ajax_json(request):
    print(request.POST)
    import time
    time.sleep(3)
    ret = {'code':True,'data':request.POST.get('username')}
    import json
    return HttpResponse(json.dumps(ret))

def upload(request):
    return render(request,'upload.html')

def upload_file(request):
    username = request.POST.get('username')
    fa = request.FILES.get('fa')
    print(request.POST)
    print(username,fa)
    import os
    img_path = os.path.join('static/image',fa.name)
    with open(img_path,'wb') as f:
        for item in fa.chunks():
            f.write(item)
    ret = {'code': True, 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))