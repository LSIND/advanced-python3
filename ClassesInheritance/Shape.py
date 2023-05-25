#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Shape:
    '''Represents a base class Shape.'''
    _name = 'no name (base)'
    _area = 0
    _perim = 0

    def __str__(self):
        '''Returns a string representation.'''
        return f'Figure: {self._name} with {self._area} area and {self._perim} perimeter'
    def ComputePerim(self):
        '''ComputePerim - 'VIRTUAL'; but it is not necessary to define it'''
        pass
    def ComputeArea(self):
        '''ComputePerim - 'VIRTUAL'; but it is not necessary to define it'''
        pass
