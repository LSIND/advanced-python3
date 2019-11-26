#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from HotDrink import HotDrink
from ICup import ICup
from zope.interface import implementer

@implementer(ICup)
class CupOfCoffee(HotDrink):
# constructor
    def __init__(self, bean = 'arabica'):
        if(bean=='arabica' or bean=='robusta'):
            self._bean = bean

#override block
    def Milk(self, milk):
        if(0 <= milk <= 10):
            self._milk = milk
        return self._milk
        #print("Added milk to coffee: ", self._milk)

    def Sugar(self, sugar):
        if(0 <= sugar <= 5):
            self._sugar = sugar
        return self._sugar
        #print("Added sugar to coffee: ", self._sugar)

    def Drink(self):
        print("Drink your coffee: ", self._bean)
    def AddMilk(self):
        print("Added milk to coffee: ", self._milk)
    def AddSugar(self):
        print("Added sugar to coffee: ", self._sugar)

#implementation block
    _type = "test"
    @property
    def Type(self):
        self._type = "pl"
        return self._type
    @property
    def Volume(self, v):
        pass
        #return self.volume
    def Refill(self):
        print("Refill cup of coffee volume")
    def Wash(self):
        print("Wash cup of coffee made of ", self._type)
