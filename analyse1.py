#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import json
path = 'chp02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

#获取所有的时区
time_zones = [rec['tz'] for rec in records if 'tf' in rec]
#print time_zones


#获取所有时区的计数
from collections import defaultdict
def get_counts(seq):
    counts = defaultdict(int) #所有的初始值都会被初始化为0
    for x in seq:
        counts[x] +=1
    return counts

counts = get_counts(time_zones)
#print counts


#获取前10位的时区及其计数值
def top_counts(count_dict,n = 10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
print top_counts(counts),'111111111'


#pandas的DataFrame，可以将数据变成一个表格
frame = DataFrame(data=records)
#print frame
print frame['tz'][:10]



#下面利用matplotlib为这段数据生成一张图片，但是在这之前需要先给记录中未知或者缺失的时区填上一个替代值。
clean_tz = frame['tz'].fillna('Missing')    #替换缺失值
clean_tz[clean_tz == ''] ='Unknown'         #空字符串
tz_counts = clean_tz.value_counts()
print tz_counts[:10]

tz_counts[:10].plot(kind='barh',rot=0)        #生成图片，一定要使用ipython的pylab模式打开
print frame['a'][1]



#将浏览器进行大致分类
results = Series([x.split()[0] for x in frame.a.dropna()])
print results[:5]


#按照windows和非windows用户对时区统计信息进行分解
cframe = frame[frame.a.notnull()]     #将agent缺失的数据移除
operating_system = np.where(cframe['a'].str.contains('windows'),
                            'Windows','Not Windows')

print operating_system[:5]
#根据时区和新得到的操作系统列表对数据进行分组
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)    #size对分组结果进行计数，利用unstack对计数结果进行重塑
print agg_counts[:10]

#选取最常出现的时区,agg_counts中的行数构造一个间接索引的数组
indexer = agg_counts.sum(1).argsort()
print indexer[:10]

#使用take截取最后10行
count_subset = agg_counts.take(indexer)[-10:]
print count_subset

count_subset.plot(kind='barh',stacked=True)    #生成一张堆积条形图
normed_subset  = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)    #将各行规范化为总计为1，并绘图

