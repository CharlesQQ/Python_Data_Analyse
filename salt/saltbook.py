#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import sys
ret = {'environment':"",'classes':[]}
Minion={'environment':'base'}
Minion01 = {'environment':'stage'}
if sys.argv[1] == 'Minion':
    ret['classes'] =['cpis']
    ret['environment'] = Minion['environment']
    print ret
else:
    ret['classes'] = ['sshd']
    ret['environment'] = Minion01['environment']
    print ret