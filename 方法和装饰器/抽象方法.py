#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError

class Sub_Pizza(Pizza):
    pass
    # @staticmethod
    # def get_radius():
    #     pass
Sub_Pizza().get_radius()

import abc

class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """return the list of radius"""
# BasePizza()
