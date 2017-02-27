#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'


#批量执行
import salt.client
local = salt.client.LocalClient()
returns = local.cmd_batch('*','state.highstate',bat='10%')
for res in returns:
    print res

#逐个返回结果
ret = local.cmd_iter('*','test.ping')
for i in ret:
    print i

#逐次返回结果，如果没有结果继续等待
ret_block = local.cmd_iter_no_block('*','cmd.run',['whoami'])
for n in ret_block:
    print n

# ret_subset = local.cmd_subset('*','test.ping',sub=1,progress=True)
# print ret_subset

#异步发送命令
ret_job = local.run_job('*','test.sleep',[10])
print ret_job


