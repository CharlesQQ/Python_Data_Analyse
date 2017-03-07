#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

# class Shape(object):
#     pass
#
# class Triangle(Shape):
#
#     def draw(self):
#         print "画三角形"
#
#
# class Square(Shape):
#
#     def draw(self):
#         print "画正方形"
#
# s1 = Triangle()
# s2 = Shape()
#
# s1.draw()
#
# s2.draw()

class Shape(object):
    def draw(self):
        raise NotImplementedError


class Circle(Shape):
  def draw(self):
    print('draw circle')

class Rectangle(Shape):
  def draw(self):
    print('draw Rectangle')

class ShapeFactory(object):    #由子类负责调用那个父类
  '''接口类，负责决定创建哪个ShapeFactory的子类'''
  def create(self, shape):
    if shape == 'Circle':
      return Circle()
    elif shape == 'Rectangle':
      return Rectangle()
    else:
      return None


fac = ShapeFactory()
obj = fac.create('Circle')
obj.draw()