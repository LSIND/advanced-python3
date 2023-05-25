#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi
from Shape import Shape

class Circle(Shape):
    """Represents class Circle."""
    def __init__(self, rad):
        self._name = 'Circle'
        self.__radius = rad

    def ComputeArea(self):
        self._area = pi *self.__radius *self.__radius
        
    def ComputePerim(self):
        self._perim = 2 * pi * self.__radius