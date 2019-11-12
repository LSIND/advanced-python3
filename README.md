# Advanced Python 3

This repository presents advanced usage of Python incl OOP implementation, working with SQL and NOSQL databases and fetching HTML data.

## Projects

Projects covering Advanced Python using **Python3.7**
- understanding classes in Python : association
- understanding classes in Python : inheritance
- understanding classes in Python : abstract class and interfaces
- creating sqlite database
- using ORM: SQLAlchemy
- creating MongoDB database
- fetching html data


## [Classes in Python: association](https://github.com/LSIND/advanced-python3/tree/master/ClassesAssociation)
> *Classes association*

Create a project which simulates shuffling of card deck (52 cards).

Class Card:
 - 2 fields: suit and rank 
 - constructor `__init__(self, suit, rank)` sets the Card
 - overrided `__str__(self)` method prints card name, f.e. "jack of hearts"

Class Deck:
- contains two lists of ranks and suits
- creates list of 52 objects of class Card
- constructor `__init__(self)` sets the Deck
- method `shuffle(self)` shuffles cards in Deck using random
- overrided `__str__(self)` method prints all cards in a deck

![UML class diagram](https://www.dropbox.com/s/4h1fwijt5k6uwwk/cards.JPG?raw=1)

## [Classes in Python: inheritance](https://github.com/LSIND/advanced-python3/tree/master/ClassesInheritance)
> *Classes inheritance*

Create a project which simulates shuffling of card deck (52 cards).

Class Shape:
 - 3 fields: name of figure, area and perimiter
 - method `ComputePerim(self)` is *virtual-like* to be overrided in derived classes - is not necessary to declare
 - method `ComputeArea(self)` is *virtual-like* to be overrided in derived classes - is not necessary to declare
 - overrided `__str__(self)` method prints figure, and its calculated area and perimiter
 
 Class Circle:
- inherits from Shape
- constructor `__init__(self, radius)` sets radius of circle
- overrided method `ComputePerim(self)` calculates the perimeter of circle
- overrided method `ComputeArea(self)` calculates the area of circle

Class Rectangle:
- inherits from Shape
- constructor `__init__(self, width, height)` sets width and height of rectangle
- overrided method `ComputePerim(self)` calculates the perimeter of rectangle
- overrided method `ComputeArea(self)` calculates the area of rectangle

Class Square:
- inherits from Rectangle
- constructor `__init__(self, width)` sets side of shape and calls the cinstructor of base class rectangle


![UML class diagram](https://www.dropbox.com/s/gsvysyhc35drt1s/Shapes.JPG?raw=1)
