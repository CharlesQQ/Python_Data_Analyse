# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-30 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170528_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserType1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo1',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserType1'),
        ),
    ]
