#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest

from count import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.obj=Count()

    def tearDown(self):
        self.obj=None

    def add_test(self):
        print 'run add_test'
        print self.obj.add(10,20)==30

    def sub_test(self):
        print 'run sub_test'
        print self.obj.sub(10,5)==5

if __name__ == '__main__':
    demo_add=TestAdd('add_test')
    demo_add.run()
    demo_sub=TestAdd('sub_test')
    demo_sub.run()