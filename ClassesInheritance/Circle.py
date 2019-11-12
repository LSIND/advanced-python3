#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from Shape import Shape

class Circle(Shape):
    """Represents class Circle."""
    def __init__(self, rad):
        self._name = 'Circle'
        self.radius = rad

    def ComputeArea(self):
        self._area = math.pi *self.radius *self.radius
        
    def ComputePerim(self):
        self._perim = 2* math.pi * self.radius