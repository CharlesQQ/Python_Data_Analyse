#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import salt.config
master_opts = salt.config.client_config('/etc/salt/master')
print  dir(master_opts)
print type(master_opts)

print(master_opts)
