#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class HotDrink(ABC):
    '''abstract class'''
    _sugar = 3
    _milk = 3
    @property
    @abstractmethod
    def Sugar(self, sugar):
        pass
    @property
    @abstractmethod
    def Milk(self, milk):
        pass

    @abstractmethod
    def Drink(self):
        pass
    @abstractmethod
    def AddMilk(self):
        pass
    @abstractmethod
    def AddSugar(self):
        pass