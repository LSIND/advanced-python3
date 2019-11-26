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
            self._leaf = leaf

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
        print("Drink your tea: ", self._leaf)
    def AddMilk(self):
        print("Added milk to tea: ", self._milk)
    def AddSugar(self):
        print("Added sugar to tea: ", self._sugar)

#implementation block
    _type = "test"
    @property
    def Type(self):
        self._type = "glass"
        return self._type
    @property
    def Volume(self, v):
        pass
        #return self.volume
    def Refill(self):
        print("Refill cup of tea volume")
    def Wash(self):
        print("Wash cup of tea")

