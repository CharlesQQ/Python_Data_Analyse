#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

# def identify(f):
#     return f
#
# @identify
# def foo():
#     return 'bar'

_function = {}
def register(f):
    global _function
    _function[f.__name__]=f
    return f

@register
def foo():
    return 'bar'

"""
class Store(object):
    def get_food(self,username,food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.get(food)

    def put_food(self,username,food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        self.storage.put(food)
"""

"""
def check_is_admin(username):
    if username != 'admin':
        raise Exception("This is not allowed to get food")

class Store(object):
    def get_food(self,username,food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self,username,food):
        check_is_admin(username)
        self.storage.put(food)
"""




def check_is_admin(f):
    def wrapper(*args,**kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args,**kwargs)
    return wrapper

class store(object):
    @check_is_admin
    def get_food(self,username,food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self,username,food):
        self.storage.put(food)
'''

def is_admin(f):
    def wrapper(*args,**kwargs):
        if kwargs.get(*args,**kwargs):
            raise Exception("This user is not allowed to get food")
        return f(*args,**kwargs)
    return wrapper

def foobar(username="someone"):
    """Do crzay staff."""
    pass
print foobar.func_doc
print foobar.func_name

# @is_admin
def foobar(username="someone"):
    """Do crazy staff"""
    pass
# print foobar.__doc__
# print foobar.__name__

import functools
foobar = functools.update_wrapper(is_admin,foobar)
print foobar.__name__
print foobar.__doc__
'''

import functools

def is_admin(f):
    @functools.wraps(f)
    def wrapper(*args,**kwargs):
        if kwargs.get(*args,**kwargs):
            raise Exception("This user is not allowed to get food")
        return f(*args,**kwargs)
    return wrapper

@is_admin
def foobar(username="someone"):
    """Do crazy staff"""
    pass
print foobar.__doc__
print foobar.__name__
