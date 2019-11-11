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


## [Classes in Python: association](https://github.com/LSIND/intro-to-python3-analysis/tree/master/ClassesAssociation)
> *Using built-in capabilities for string data processing*

Create a project which simulates shuffling of card deck (52 cards).

Class Card:
 - 2 fields: suit and rank 
 - constructor __init__ sets the Card
 - overrided __str__ method prints card name, f.e. "jack of hearts"

Class Deck:
- creates list of 52 objects of class Card
- constructor __init__ sets the Deck
- method Shuffle shuffles cards in Deck using random
- overrided __str__ method prints all cards f a deck

![UML class diagram](https://www.dropbox.com/s/4h1fwijt5k6uwwk/cards.JPG?raw=1)
