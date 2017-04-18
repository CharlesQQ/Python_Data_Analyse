#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import sys
import subprocess
import re
import datetime

def read_stdin():
    data=sys.stdin.read().strip()
    if data:
        return data
    else:
        exit(u'没有标准输入')

def bash(cmd):
    return subprocess.call(cmd, shell=True)

def get_starttime(data):
    time_str=''
    for line in data.split('\n'):
        if line.__contains__('Log opened'):
            time_str=line.strip().split()[-1]
            print time_str
            print time_str.strip('Z')
            break
    try:
        year,mouth,day,hour,minute,second,microsecond=map(int,re.split('\-|T|\,|\:|\.',time_str.strip('Z')))
        return datetime.datetime(year=year,month=mouth,day=day,hour=hour,minute=minute,second=second)
    except Exception,e:
        print u"bash命令执行错误，获取起始时间出错"

def get_log_line_time(data):
    start_time=get_starttime(data=data)
    print data
    for line in data.split('\n'):
        try:
            time_str=line.split()[0]
            hour,minute,second,microsecond=map(int,re.split('\:|\.| |',time_str.strip())[:4])
            log_line_time=start_time+datetime.timedelta(hours=hour,minutes=minute,
                                                        seconds=second)
            real_time_str=log_line_time.strftime('%Y-%m-%d %H:%M:%S %f')
            line=line.replace(time_str,real_time_str)
            print line
        except Exception,e:
            print e
            # continue

if __name__ == '__main__':
    get_log_line_time(read_stdin())
