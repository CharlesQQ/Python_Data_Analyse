#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

"""
class Pizza(object):
    def __init__(self,size):
        self.size = size

    def get_size(self):
        return self.size

#print (Pizza.get_size)
print (Pizza.get_size.__self__)
"""

class Pizza(object):
    def __init__(self,cheese,vegetables):
        self.cheese = cheese
        self.vegetables= vegetables
    @staticmethod
    def min_ingredient(x,y):
        return x+y

    def cook(self):
        return self.min_ingredient(self.cheese,self.vegetables)

# print Pizza('t1','t2').cook() is Pizza('t1','t2').cook()
# print Pizza('t1','t2').min_ingredient is Pizza.min_ingredient
# print Pizza('t1','t2').min_ingredient is Pizza('t1','t2').min_ingredient

class Sub_Pizza(Pizza):
    pass


class Pizza_1(object):
    radius = 12
    @classmethod
    def get_radius(cls):
        print cls
        return cls.radius

# print Pizza_1.get_radius
# print Pizza_1().get_radius

print (Pizza_1.get_radius is Pizza_1().get_radius)
print Pizza_1.get_radius()


class MyPizza(object):
    def __init__(self,ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls,fridge):
        return cls(fridge.get_cheese()+fridge.get_vegetables())
