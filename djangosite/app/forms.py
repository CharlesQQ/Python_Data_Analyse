#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

from django.forms import ModelForm
from models import Moment

class MomentForm(ModelForm):
    class Meta:
        model = Moment     #声明与其表单关联的模型类及其字段
        fields = '__all__'    #导入所有字段,相同于('content','user_name','kind')
