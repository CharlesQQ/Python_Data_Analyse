#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

farm=sorted(['haystack','needle','cow','pig'])
print farm
import bisect
print bisect.bisect(farm,'needle')
print bisect.bisect_left(farm,'needle')
print bisect.bisect_left(farm,'eggs')