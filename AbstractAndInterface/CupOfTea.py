#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zope.interface import implementer
from HotDrink import HotDrink
from ICup import ICup

@implementer(ICup)
class CupOfTea(HotDrink):
# constructor
    def __init__(self, leaf = 'black'):        
        if(leaf == 'green' or leaf == 'black'):
            self.__leaf = leaf
        else:
            self.__leaf = 'black'
            print(f'{leaf} is not an available leaf type. Setting default: {self.__leaf}')

#override block
    def Milk(self, milk):
        if(0 <= milk <= 3):
            self._milk = milk
        return self._milk

    def Sugar(self, sugar):
        if(0 <= sugar <= 10):
            self._sugar = sugar
        return self._sugar

    def Drink(self):
        print(f'Drink your tea: {self.__leaf}')
    def AddMilk(self):
        print(f'Added milk to tea: {self._milk}')
    def AddSugar(self):
        print(f'Added sugar to tea: {self._sugar}')

#implementation block
    __type = 'test'
    __vol = 0.5

    @property
    def Type(self):
        return self.__type
    @Type.setter
    def Type(self, t):
        self.__type = t
        
    @property
    def Volume(self):
        return self.__vol
    @Volume.setter
    def Volume(self, v):
        self.__vol= v
        
    def Refill(self):
        print(f'Refill cup of TEA volume {self.__vol}')
    def Wash(self):
        print(f'Wash cup of TEA made of {self.__type}')