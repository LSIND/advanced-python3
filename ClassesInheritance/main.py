#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Rectangle import Rectangle
from Circle import Circle
from Square import Square

if __name__ == '__main__':
    print("All shapes: ")
    r = Rectangle(20, 40)
    r.ComputeArea()
    r.ComputePerim()
    print(r)

    c = Circle(4)
    c.ComputeArea()
    c.ComputePerim()
    print(c)

    s = Square(5)
    s.ComputeArea()
    s.ComputePerim()
    print(s)
