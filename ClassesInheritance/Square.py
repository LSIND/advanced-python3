#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Rectangle import Rectangle

class Square(Rectangle):
    '''Represents class Square.'''
    def __init__(self, side):        
        Rectangle.__init__(self, side, side) # calling constructor of base class
        self._name = 'Square'