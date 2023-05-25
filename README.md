# Advanced Python 3

This repository presents advanced usage of Python incl OOP (object-oriented programming) implementation, working with relational databases and NOSQL databases + fetching HTML data.

## Projects
Projects covering Advanced Python using **Python3.7**
- classes in Python : association
- classes in Python : inheritance
- classes in Python : abstract classes and interfaces
- fetching html data: BeautifulSoup
- using sqlite database
- using ORM: SQLAlchemy
- working with MongoDB database

## [Classes in Python: association](https://github.com/LSIND/advanced-python3/tree/master/ClassesAssociation)
> *Classes association*

Project which simulates shuffling of card deck (52 cards). You should print sorted deck of cards, after shuffle it and print again.

Class Card:
 - constructor `__init__(self, suit, rank)` sets the Card
 - overrided `__str__(self)` method prints card name, f.e. "jack of hearts"

Class Deck:
- contains two lists of ranks and suits
- constructor `__init__(self)` sets the Deck: creates list of 52 objects of class Card
- method `shuffle(self)` shuffles cards in Deck using random
- overrided `__str__(self)` method prints all cards in a deck

![UML class diagram](https://www.dropbox.com/s/4h1fwijt5k6uwwk/cards.JPG?raw=1)

## [Classes in Python: inheritance](https://github.com/LSIND/advanced-python3/tree/master/ClassesInheritance)
> *Classes inheritance*

Project with class hierarchy: reusing methods of base classes. *In Python it is not necessary to declare virtual methods

Class Shape:
 - 3 default fields: name of figure, area and perimiter
 - method `ComputePerim(self)` is *virtual-like* to be overrided in derived classes
 - method `ComputeArea(self)` is *virtual-like* to be overrided in derived classes
 - overrided `__str__(self)` method prints figure name and its calculated area and perimiter
 
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
- constructor `__init__(self, width)` sets side of shape and calls the cinstructor of base class rectangle (constructor chaining).


![UML class diagram](https://www.dropbox.com/s/gsvysyhc35drt1s/Shapes.JPG?raw=1)

## [Abstract classes and interfaces in Python](https://github.com/LSIND/advanced-python3/tree/master/AbstractAndInterface)
> Declaration of abstract class and interface in python3   
> *This task and UML class diagram were taken from C# / Java project to draw an analogy between OOP style in Python and OOP in C#/Java. From this case it's clear that interfaces in Python are a little bit useless: Python has a multiple inheritance, C#/Java - single*

*ABC* (abstract class) is a part of Python Standart Library.  
As for interfaces, module *zope* can be used.
```Console
pip install zope
```

**Class HotDrink (abstract)**:
```python
from abc import ABC, abstractmethod
```
- 2 protected fields: milk = 3, sugar = 3 (default values for derived classes)
- 2 abstract properties: Milk, Sugar
- 3 abstract methods: AddMilk, AddSugar, Drink
- all class members which have `@abstractmethod` decorator MUST be overrided in child classes.   
**Interface ICup**:
```python
from zope.interface import Interface, Attribute
```
- 2 properties
- 2 methods.   
**Class CupOfCoffee**:  
- implements ICup interface  
- inherits abstract class HotDrink  
- has its own property BeanType: arabica or robusta
```python
@implementer(ICup)
class CupOfCoffee(HotDrink):
    pass
```
**Class CupOfTea**:  
- implements ICup interface  
- inherits abstract class HotDrink  
- has its own property LeafType: green or black
```python
@implementer(ICup)
class CupOfTea(HotDrink):
    pass
```

![UML class diagram](https://www.dropbox.com/s/hq54ixgzff12kip/Abstr_Int.JPG?raw=1)

## [Python Text Web Scraping](https://github.com/LSIND/advanced-python3/tree/master/FullMoonDatetime)
> BeautifulSoup + static content   
> Get Full Moon Calendar data from [fullmoon.info web site](https://www.fullmoon.info/en/fullmoon-calendar_1900-2050.html) for 150 years. Every year is presented in separate page:
`https://www.fullmoon.info/en/fullmoon-calendar/`X, where X is a year.
> create table and insert fetched data fetched into sqlite database.

1. Install packages:  
```Console
pip install beautifulsoup4
pip install requests
```
*Beautiful Soup (bs4)* = Python library for pulling data out of HTML and XML files.  
*requests* = HTTP library  
*sqlite3* = Python standard library contains the SQLite module.

2. Create function which takes list of years and scrapes every of 150 pages. Every html-page consists of such span-block, f.e. for `https://www.fullmoon.info/en/fullmoon-calendar/1901.html`:
```HTML
<table class="table-calendar">
<tbody>
    <tr><td class="weekday">Saturday</td><td class="date">5 January 1901</td><td class="time">1:13:24 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Sunday</td><td class="date">3 February 1901</td><td class="time">4:29:42 pm</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Tuesday</td><td class="date">5 March 1901</td><td class="time">9:04:06 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Thursday</td><td class="date">4 April 1901</td><td class="time">2:20:06 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Friday</td><td class="date">3 May 1901</td><td class="time">7:18:42 pm</td><td class="notes">&nbsp;[/]</td></tr>
    <tr><td class="weekday">Sunday</td><td class="date">2 June 1901</td><td class="time">10:52:42 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Tuesday</td><td class="date">2 July 1901</td><td class="time">12:17:36 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Wednesday</td><td class="date">31 July 1901</td><td class="time">11:33:42 am</td><td class="notes">&nbsp;[+]</td></tr>
    <tr><td class="weekday">Thursday</td><td class="date">29 August 1901</td><td class="time">9:20:48 pm</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Saturday</td><td class="date">28 September 1901</td><td class="time">6:35:42 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Sunday</td><td class="date">27 October 1901</td><td class="time">4:06:12 pm</td><td class="notes">&nbsp;[*]</td></tr>
    <tr><td class="weekday">Tuesday</td><td class="date">26 November 1901</td><td class="time">2:17:30 am</td><td class="notes">&nbsp;</td></tr>
    <tr><td class="weekday">Wednesday</td><td class="date">25 December 1901</td><td class="time">1:15:48 pm</td><td class="notes">&nbsp;</td></tr>
</tbody>
</table>
```
We need to get `class="table-calendar"`.

3. You can find full csv dataset on my Kaggle page: [Full Moon Calendar 1900-2050](https://www.kaggle.com/lsind18/full-moon-calendar-1900-2050)
4. Before inserting data into database we need to convert date and time in one object: 5 January 1901 1:13:24 am -> 1901-01-05 01:13:24


## [Python Images Web Scraping](https://github.com/LSIND/advanced-python3/tree/master/GemstonesImages)
> BeautifulSoup + static content       
> Fetch data from [minerals.net](https://www.minerals.net): create folders with gemstones names and download images of them in each coresponding folder.  

1. Get the page with [list of all gemstones](https://www.minerals.net/GemStoneMain.aspx) and find HTML-element with them:
```python
page = 'https://www.minerals.net/GemStoneMain.aspx'
resp = requests.get(page)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        table_gems=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```
3. Parse links to the pages of each gemstone and create a dictionary {gemstone name : link }

4. Parse each page to get pictures of gemstones
```python
table_images=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```
You can find full gemstones images dataset from multiple sources on my Kaggle page: [Gemstones Images](https://www.kaggle.com/lsind18/gemstones-images)

## [Gismeteo Web Scraping + SQLAlchemy](https://github.com/LSIND/advanced-python3/tree/master/GismeteoSqlAlchemy)
> BeautifulSoup + SQLite       
> Fetch data from [gismeteo.ru](https://www.gismeteo.ru): city + period and put it into database using ORM sqlalchemy v2

1. Install packages:  
```Console
pip install beautifulsoup4
pip install sqlalchemy
```

2. Get example page [weather in Moscow 14 days](https://www.gismeteo.ru/weather-moscow-4368/2-weeks/) and find HTML-element with class `widget-items`.
3. Get day of week, date, description, temperature (max), temperature (min), wind (m/s), wind direction, precipitation, humidity, radiation.
4. Create class Weather with corresponding fields.
5. Create SqlAlchemy Engine (connection), SqlAlchemy Table with 10 columns and mapper between class Weather and SqlAlchemy Table.
6. Process data from site to be string, date, float etc and put it into database. Aware of duplicates.


## [Python + MongoDB](https://github.com/LSIND/advanced-python3/tree/master/MongoDbProvider)
> *Working with nosql database using python*  
> basic operations working with MongoDB using pymongo.
```Console
pip install pymongo
```
*opt: download and install GUI [Compass](https://www.mongodb.com/products/compass)*

The sample database is [weather.json](https://atlas-data-lake.s3.amazonaws.com/json/sample_weatherdata/data.json). Import data into MongoDB instance and check the collection: **Schema -> Analyze**.  

Using Compass check data:  
```Console
{"airTemperature.value": 3}
{"airTemperature.value": {$gt: 10}}
{"wind.type": {$ne: "N"}}
{"atmosphericPressureChange" : {$exists: true}}
```

Simple examples of CRUD operations in MongoDB using pymongo: ```insert_one (insert_many), find, update_one (update_many), delete_one (delete_many)```.  
All these methods expect dictionary/dictionaries as a parameter(s).