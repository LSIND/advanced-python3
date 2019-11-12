#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Rectangle, Circle, Square

if __name__ == '__main__':
    print("All shapes: ")
    r = Rectangle.Rectangle(20, 40)
    r.ComputeArea()
    r.ComputePerim()
    print(r)
    
    c = Circle.Circle(4)
    c.ComputeArea()
    c.ComputePerim()
    print(c)
    s = Square.Square(5)
    s.ComputeArea()
    s.ComputePerim()
    print(r)
