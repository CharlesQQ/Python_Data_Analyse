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

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] ='Unknown'
tz_counts = clean_tz.value_counts()
print tz_counts[:10]


