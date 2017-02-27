#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import salt.config
opts= salt.config.master_config('/etc/salt/master')
runner = salt.runner.RunnerClient(opts)
print runner.cmd('job.list_jobs',[])