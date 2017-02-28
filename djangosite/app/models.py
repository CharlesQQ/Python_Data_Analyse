#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

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

