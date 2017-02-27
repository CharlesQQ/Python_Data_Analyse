#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import salt.client
local = salt.client.LocalClient()
res = local.cmd('*','cmd.run',['whoami'])
print res

res1 =local.cmd('*',[
    'grains.items',
    'sys.doc',
    'cmd.run',
],
[               [],
                [],
                ['uptime'],
])
# print res1

res3 = local.cmd_async('*','cmd.run','ls')    #异步执行，返回的是jid(任务id)
print res3