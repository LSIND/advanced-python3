# Advanced Python 3

This repository presents advanced usage of Python incl OOP implementation, working with SQL and NOSQL databases and fetching HTML data.

## Projects
Projects covering Advanced Python using **Python3.7**
- classes in Python : association
- classes in Python : inheritance
- classes in Python : abstract classes and interfaces
- fetching html data: BeautifulSoup
- creating sqlite database
- using ORM: SQLAlchemy
- creating MongoDB database

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

## [Abstract classes and interfaces in Python](https://github.com/LSIND/advanced-python3/tree/master/AbstractAndInterface)
> *Declaration of abstract class and interface in python3*

ABC (abstract class) is a part of Python Standart Library.  
As for interfaces, module *zope* can be used.
```Console
pip install zope
```

**Class HotDrink (abstract)**:
```python
from abc import ABC, abstractmethod
```
**Interface ICup**:
```python
from zope.interface import Interface, Attribute
```
**Class CupOfCoffee**:  
implements ICup interface  
inherits abstract class HotDrink  
has its own property BeanType: arabica or robusta
```python
@implementer(ICup)
class CupOfCoffee(HotDrink):
    pass
```
**Class CupOfTea**:  
implements ICup interface  
inherits abstract class HotDrink  
has its own property LeafType: green or black
```python
@implementer(ICup)
class CupOfTea(HotDrink):
    pass
```

## [Python Text Web Scraping](https://github.com/LSIND/advanced-python3/tree/master/FullMoonDatetime)
> BeautifulSoup + static content   

Get Full Moon Calendar data from [fullmoon.info web site](https://www.fullmoon.info/en/fullmoon-calendar_1900-2050.html) for 150 years. Every year is presented in separate page:
`https://www.fullmoon.info/en/fullmoon-calendar/`X, where X is a year.

1. Install packages:  
```Console
pip install bs4
pip install requests
```
*Beautiful Soup (bs4)* = Python library for pulling data out of HTML and XML files.  
*requests* = HTTP library

2. Create function which takes list of years and scrapes every of 150 pages. Every html-page consists of such span-block, f.e. for `https://www.fullmoon.info/en/fullmoon-calendar/1901`:
```HTML
<span class="text-normal">
    Saturday, 5 January 1901, 01:13:24 am<br>
    Sunday, 3 February 1901, 04:29:42 pm<br>
    Tuesday, 5 March 1901, 09:04:06 am<br>
    Thursday, 4 April 1901, 02:20:06 am<br>
    ......
    Tuesday, 26 November 1901, 02:17:30 am<br>
    Wednesday, 25 December 1901, 01:15:48 pm<br><br>
    <br>
    <i>Time specification for Central Europe</i><br>
</span>
```
Span element does not have id so we can use a selector to parse it:
```python
url = 'https://www.fullmoon.info/en/fullmoon-calendar/'
html = requests.get(url+'1901').text
soup = bs(html, 'html.parser')
selector = 'tr span'
rows = soup.select(selector)
```

3. Page of current year has a different structure and needed data is placed in `div` block.   
You can find full dataset on my Kaggle page: [Full Moon Calendar 1900-2050](https://www.kaggle.com/lsind18/full-moon-calendar-1900-2050)


## [Python Images Web Scraping](https://github.com/LSIND/advanced-python3/tree/master/GemstonesImages)
> BeautifulSoup + static content      

Fetch data from [minerals.net](https://www.minerals.net): create folders with gemstones names and download images of them in each coresponding folder.  

1. Get the page with [list of all gemstones](https://www.minerals.net/GemStoneMain.aspx) and find HTML-element with them:
```python
url = 'https://www.minerals.net/GemStoneMain.aspx'
html = requests.get(url).text
soup = bs(html, 'html.parser')
table_gems=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```
3. Parse links to the pages of each gemstone and create dictionary {gemstone name : link }

4. Parse each page to get pictures of gemstones
```python
table_images=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```
You can find full gemstones images dataset from multiple sources on my Kaggle page: [Gemstones Images](https://www.kaggle.com/lsind18/gemstones-images)

## [Python + SQLite Database](https://github.com/LSIND/advanced-python3/tree/master/PythonSqlite)
> *Working with sqlite database using python*

Python standard library contains the SQLite module.

Create a simple database for [fetched data of Full Moons](https://github.com/LSIND/advanced-python3/tree/master/FullMoonDatetime)
```python
import sqlite3
from sqlite3 import Error
```

Check database structure with [DB Browser for SQLite](https://sqlitebrowser.org/)


## [Python + MongoDB](https://github.com/LSIND/advanced-python3/tree/master/PythonMongoDB)
> *Working with nosql database using python*
```Console
pip install pymongo
```
