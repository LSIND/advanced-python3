#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Shape import Shape

class Rectangle(Shape):
    '''Represents class Rectangle.'''
    def __init__(self, length, width):
        self._name = 'Rectangle'
        self.__length = length
        self.__width = width

    def ComputeArea(self):
        self._area = self.__length * self.__width
        
    def ComputePerim(self):
        self._perim = 2*(self.__length + self.__width)