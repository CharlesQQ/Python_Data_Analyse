#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'


import salt.client
minion_opts = salt.config.minion_config('/etc/salt/minion')
print dir(minion_opts)
print (minion_opts)

print(minion_opts.keys())
print(minion_opts['user'])