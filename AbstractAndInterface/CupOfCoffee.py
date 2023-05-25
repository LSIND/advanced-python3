#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zope.interface import implementer
from HotDrink import HotDrink
from ICup import ICup

@implementer(ICup)
class CupOfCoffee(HotDrink):
# constructor
    def __init__(self, bean = 'arabica'):
        if(bean=='arabica' or bean=='robusta'):
            self.__bean = bean
        else:
            self.__bean = 'arabica'
            print(f'{bean} is not an available bean type. Setting default: {self.__bean}')

#override block
    def Milk(self, milk):
        if(0 <= milk <= 10):
            self._milk = milk
        return self._milk

    def Sugar(self, sugar):
        if(0 <= sugar <= 5):
            self._sugar = sugar
        return self._sugar

    def Drink(self):
        print(f'Drink your coffee: {self.__bean}')
    def AddMilk(self):
        print(f'Added milk to coffee: {self._milk}')
    def AddSugar(self):
        print(f'Added sugar to coffee: {self._sugar}')

#implementation block
    __type = 'plastic'
    __vol = 0.2
    
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
        print(f'Refill cup of COFFEE volume {self.__vol}')
    def Wash(self):
        print(f'Wash cup of COFFEE made of {self.__type}')
