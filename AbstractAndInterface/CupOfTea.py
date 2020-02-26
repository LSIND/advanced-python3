#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from HotDrink import HotDrink
from ICup import ICup
from zope.interface import implementer

@implementer(ICup)
class CupOfTea(HotDrink):
# constructor
    def __init__(self, leaf = 'black'):
        if(leaf=='green' or leaf=='black'):
            self.__leaf = leaf

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
        print("Drink your tea: ", self.__leaf)
    def AddMilk(self):
        print("Added milk to tea: ", self._milk)
    def AddSugar(self):
        print("Added sugar to tea: ", self._sugar)

#implementation block
    __type = "test"
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
        print("Refill cup of tea volume", self.__vol)
    def Wash(self):
        print("Wash cup of TEA made of ", self.__type)
