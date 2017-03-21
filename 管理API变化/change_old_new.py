#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import warnings
class Car(object):
    def turn_left(self):
        """
        This is old API version
        :return:
        """
        warnings.warn("turn left is deprecated,use turn instead",DeprecationWarning)
        return  self.turn(direction="left")

    def turn(self,direction):
        print "This is turn method"

car = Car()
car.turn_left()