#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Shape import Shape

class Rectangle(Shape):
    """Represents class Rectangle."""
    def __init__(self, length, width):
        self._name = 'Rectangle'
        self.length = length
        self.width = width

    def ComputeArea(self):
        self._area = self.length * self.width
        
    def ComputePerim(self):
        self._perim = 2*(self.length + self.width)