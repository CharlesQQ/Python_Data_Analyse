#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.db.models import Field    #所有普通字段类型都是继承自Fiel
# Create your models here.

KIND_CHOICES = (
    ('PYTHON技术','python技术'),
    ('数据库技术','数据库技术'),
    ('经济学','经济学'),
    ('个人心情','个人心情'),
    ('其他','其他')
)


class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20,default='匿名')
    kind = models.CharField(max_length=20,choices=KIND_CHOICES,
                            default=KIND_CHOICES[0])
    class Meta:
        db_table = "moment_table"    #定义数据库表名

aa = Moment.objects.all()

class Account(models.Model):
    user_name = models.CharField(max_length=80)
    password = models.CharField(max_length=255)
    reg_date = models.DateField()

    def __unicode__(self):
        return "Account: %s"%self.user_name

class Contact(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)    #cascade 表示级联操作，就是说，
    # 如果主键表中被参考字段更新，外键表中也更新，主键表中的记录被删除，外键表中改行也相应删除
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s, %s"%(self.account.user_name,self.mobile)

#1、抽象类继承
class MessageBase(models.Model):
    id = models.AutoField()
    content = models.CharField(max_length=100)
    user_name = models.CharField(max_length=80)
    pub_date = models.DateField()

    class Meta:
        abstract = True     #定义本类为抽象基类

class Moment1(MessageBase):
    headline = models.CharField(max_length=50)
