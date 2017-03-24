#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import abc

class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """Return the ingredient list"""

# class Calzone(BasePizza):
#
#     def get_radius(self,with_egg=False):
#         egg = Egg() if with_egg else None
#         return self.ingredient + [egg]
#
# class Egg(object):
#     pass

class DietPizza(BasePizza):

    @staticmethod
    def get_radius(self):
        return None
# # DietPizza.get_radius('xx')
#     pass
DietPizza()