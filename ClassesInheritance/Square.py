#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Rectangle import Rectangle

class Square(Rectangle):
    """Represents class Square."""
    def __init__(self, width):
        self._name = 'Square'
        Rectangle.__init__(self, width, width) # calling constructor of base class
