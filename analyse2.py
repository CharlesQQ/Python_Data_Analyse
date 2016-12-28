#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import pandas as pd
#通过pandas.read-table将各个表分别读到一个pandas DataFrame对象中
unames = ['user_id','gender','age','occuption','zip']
users = pd.read_table('ml-1m/users.dat',sep='::',header=None,names = unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('ml-1m/ratings.dat',sep='::',header=None,names= rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('ml-1m/movies.dat',sep='::',header=None,names = mnames)
print users[:5]
print movies[:5]
print ratings


#如果需要根据性别和年龄计算某部电影的平均得分，就需要将所有的数据都合并到一个表中；
#使用pandas的merge函数将ratings和users合并到一起，然后再将movies也合并进去。
data = pd.merge(pd.merge(ratings,users),movies)
print data
print "========="
print data.ix[0]