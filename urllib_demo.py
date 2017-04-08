#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import urllib2
import urllib

URL_IP='http://192.168.74.20:8000/ip'

def use_simple_urllib2():
    response=urllib2.urlopen(URL_IP)
    print ">>>>Response Headers:"
    print response.info()
    print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    print ">>>Use Simple urllib2"
    use_simple_urllib2()