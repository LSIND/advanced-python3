#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute

class ICup(Interface):
    """ICup interface"""

    Type = Attribute("The type of a cup")
    Volume = Attribute("The volume of a cup")
    def Refill():
        """Refill message"""
    def Wash():
        """Wash message"""