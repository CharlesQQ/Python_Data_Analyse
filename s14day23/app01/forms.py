#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from app01 import models
from django.forms import fields
from django.forms import widgets
from django.forms import forms
from django.forms.models import ModelChoiceField,ModelMultipleChoiceField

class UserInfoForm(forms.Form):
    user = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={'class':'c1'})
    )

    pwd = fields.CharField(
        max_length=12,
        widget=widgets.PasswordInput(attrs={'class':'c1'})
    )

    user_type=fields.ChoiceField(
        # choices=[(1,'普通用户'),(2,'超级用户'),],
        # choices=models.UserType.objects.values_list('id','name'),
        choices=[],
        widget=widgets.Select,
    )

    user_type2 = fields.CharField(
        widget=widgets.Select(choices=[])
    )

    user_type3 = ModelChoiceField(
        empty_label='请选择用户',
        queryset=models.UserType.objects.all(),
        to_field_name='name',
    )
    def __init__(self,*args,**kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id', 'name')
        self.fields['user_type2'].widget.choices = models.UserType.objects.values_list('id', 'name')
    #验证(*)
    #生成html(保留上一次提交的数据)

    #新URL方式操作(Form方式提交)
    #Ajax(可以不使用生成html的功能，也可以使用)

from django.core.exceptions import ValidationError
class RegisterForm(forms.Form):
    user = fields.CharField()
    email = fields.EmailField()

    def clean_user(self):   #如果user的正则表达式通过之后，执行user_clean方法
        c = models.UserInfo.objects.filter(name=self.cleaned_data['user']).count()
        if not c:
            return self.cleaned_data['user']
        else:
            raise ValidationError('用户名已经存在',code='xxxx')

    def clean_email(self):
        return self.cleaned_data['email']


class LoginForm(forms.Form):
    user = fields.CharField()
    pwd = fields.CharField(validators=[])

    def clean_user(self):  # 如果user的正则表达式通过之后，执行user_clean方法
        c = models.UserInfo.objects.filter(name=self.cleaned_data['user']).count()
        if not c:
            return self.cleaned_data['user']
        else:
            raise ValidationError('用户名已经存在', code='xxxx')

    def clean_pwd(self):
        return self.cleaned_data['pwd']

    def clean(self):
        c = models.UserInfo.filter(name=self.cleaned_data['user'],pwd=self.cleaned_data['pwd']).count()
        if c:
            return self.cleaned_data
        else:
            raise ValidationError('用户名或者密码错误')

    def _post_clean(self):
        pass