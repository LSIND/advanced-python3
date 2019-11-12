#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Shape:
    """Represents a base class Shape."""
    _name = 0
    _area = 0
    _perim = 0

    def __str__(self):
        """Returns a string representation."""
        return 'Figure: %s with %s area and perimeter %s' % (self._name, self._area, self._perim)
    def ComputePerim(self):
        """ComputePerim - 'VIRTUAL'; but it is not necessary to define it"""
        pass
    def ComputeArea(self):
        """ComputePerim - 'VIRTUAL'; but it is not necessary to define it"""
        pass

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


class Square(Rectangle):
    """Represents class Square."""
    def __init__(self, width):
        self._name = 'Sqaure'
        Rectangle.__init__(self, width, width)


import math

class Circle(Shape):
    """Represents class Circle."""
    def __init__(self, rad):
        self._name = 'Circle'
        self.radius = rad

    def ComputeArea(self):
        self._area = math.pi *self.radius *self.radius
        
    def ComputePerim(self):
        self._perim = 2* math.pi * self.radius



if __name__ == '__main__':
    print("Rectangle: ")
    r = Rectangle(20, 40)
    r.ComputeArea()
    r.ComputePerim()
    print(r)
    
    c = Circle(4)
    c.ComputeArea()
    c.ComputePerim()
    print(c)
    r = Square(5)
    r.ComputeArea()
    r.ComputePerim()
    print(r)