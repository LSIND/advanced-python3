# Расширенные возможности Python 3

Репозиторий содержит расширенные возможности языка Python версии **3.7** и выше (**Reviewed on 3.11**).

## Проекты
Проекты данного репозитория охватывают:
- ООП. Классы: ассоциация
- ООП. Классы: наследование
- ООП. Классы: абстрактный класс и интерфейс
- Парсинг html-данных: BeautifulSoup
- Работа с БД sqlite
- Использование ORM: SQLAlchemy
- Работа с БД MongoDB

## [Классы: ассоциация](https://github.com/LSIND/advanced-python3/tree/master/ClassesAssociation)
> *Понятие класса, его членов, а также объектов и вложенных объектов*

Проект эмулирует перемешивание игральной карточной колоды (52 карты). Требуется вывести отсортированную колоду карт, перемешать ее и вывести перемешанную.

**Class Card** (карта):
 - конструктор `__init__(self, suit, rank)` создает объект карты
 - переопределенный метод `__str__(self)` выводит имя карты, например "jack of hearts"

**Class Deck** (колода):
- содержит два поля (списки) ранга и масти карты
- конструктор `__init__(self)` создает объект колоды: список 52 объектов класса Card
- метод `shuffle(self)` перемешивает карты в колоде с использованием модуля random
- переопределенный метод `__str__(self)` выводит список карт в колоде

**Диаграмма классов**:

![UML class diagram](https://www.dropbox.com/s/4h1fwijt5k6uwwk/cards.JPG?raw=1)

## [Классы: наследование](https://github.com/LSIND/advanced-python3/tree/master/ClassesInheritance)
> *Понятие наследования. Переопределение методов родительского класса*

Проект определяет иерархию классов и переиспользование методов родительских классов (*в Python не требуется объявлять методы виртуальными*).

**Class Shape** (фигура):
 - 3 поля по умоланию (potected): имя фигурыe, площадь и периметр
 - метод `ComputePerim(self)` *virtual-like* (для переопределения в классе-наследнике) - необязателен
 - метод `ComputeArea(self)` *virtual-like* (для переопределения в классе-наследнике) - необязателен
 - переопределенный метод `__str__(self)` выводит имя фигуры и вычисленные площадь и периметр
 
 **Class Circle** (круг):
- наследник класса Shape
- конструктор `__init__(self, radius)` задает радиус круга
- overrided method `ComputePerim(self)` вычисляет длину окружности
- overrided method `ComputeArea(self)` вычисляет площадь круга

**Class Rectangle** (прямоугольник):
- наследник класса Shape
- конструктор `__init__(self, width, height)` задает ширину и высоту прямоугольника
- переопределенный метод `ComputePerim(self)` вычисляет периметр прямоугольника
- переопределенный метод `ComputeArea(self)` вычисляет площадь прямоугольника

**Class Square** (квадрат):
- наследник класса Rectangle
- конструктор `__init__(self, width)` задает сторону квадрата и вызывает конструктор родительского класса (constructor chaining).

**Диаграмма классов**:
![UML class diagram](https://www.dropbox.com/s/gsvysyhc35drt1s/Shapes.JPG?raw=1)

## [Абстрактные классы и интерфейсы](https://github.com/LSIND/advanced-python3/tree/master/AbstractAndInterface)
> Понятие абстрактного класса. Обязательное переопределение методов абстрактного класса. Использование свойств.   
> *Данный проект и UML-диаграмма были взяты из примера для C#/Java, чтобы провести аналогию между ООП подходом в Python и C#/Java. Понятие интерфейса в Python излишне: Python использует множественное наследование, а C#/Java - одиночное. Пример с интерфейсом включен в проект только в качестве лабораторного примера.*

Модуль *ABC* (abstract class) входит в Python Standart Library. Для интерфейсов можно использовать модуль *zope*.
```Console
pip install zope
```

**Class HotDrink** (абстрактный, напиток):
```python
from abc import ABC, abstractmethod
```
- 2 защищенных поля: milk = 3, sugar = 3 (значения по умолчанию для классов-наследниов)
- 2 абстратных свойства: Milk, Sugar
- 3 абстратных метода: AddMilk, AddSugar, Drink
- все члены класса с атрибутом декоратора `@abstractmethod` ДОЛЖНЫ быть переопределены в классах-наследниках.   

**Interface ICup** (интерфейс, емкость):
```python
from zope.interface import Interface, Attribute
```
- 2 свойства
- 2 метода

**Class CupOfCoffee** (чашка кофе):  
- реализует интерфейс ICup  
- наследник абстрактного класса HotDrink  
- определяет собственное свойство BeanType: arabica или robusta
```python
@implementer(ICup)
class CupOfCoffee(HotDrink):
    pass
```
**Class CupOfTea**:  
- реализует интерфейс ICup  
- наследник абстрактного класса HotDrink  
- определяет собственное свойство LeafType: green или black
```python
@implementer(ICup)
class CupOfTea(HotDrink):
    pass
```

**Диаграмма классов**:  
![UML class diagram](https://www.dropbox.com/s/hq54ixgzff12kip/Abstr_Int.JPG?raw=1)

## [Парсинг веб-контента (текст)](https://github.com/LSIND/advanced-python3/tree/master/FullMoonDatetime)
> BeautifulSoup + static content   
> Парсинг календаря полнолуний [fullmoon.info web site](https://www.fullmoon.info/en/fullmoon-calendar_1900-2050.html) за 150 лет. Каждый год с данными о полнолуниях отображается на отдельной странице: `https://www.fullmoon.info/en/fullmoon-calendar/`X, где X - год от 1900 до 2050.  
> Записать данные в текстовый файл  
>Записать данные в таблицу БД sqlite 

1. Установка библиотек:  
```Console
pip install beautifulsoup4
pip install requests
```
*Beautiful Soup (bs4)* = библиотека для парсинга HTML и XML.  
*requests* = библиотека HTTP  
*sqlite3* = входит в Python standard library.

2. Функция с параметром (список годов) для получения данных со 150 страниц. Каждая html-страница содержит span, например для `https://www.fullmoon.info/en/fullmoon-calendar/1901.html`. Требуется получить `class="table-calendar"`:
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
3. Полный набор данных в .csv: [Full Moon Calendar 1900-2050](https://www.kaggle.com/lsind18/full-moon-calendar-1900-2050)
4. Перед записью данных в таблицу БД требуется сконвертировать дату и время в один объект: `5 January 1901 1:13:24 am -> 1901-01-05 01:13:24`.


## [Парсинг веб-контента (изображения)](https://github.com/LSIND/advanced-python3/tree/master/GemstonesImages)
> BeautifulSoup + static content       
> Загрузка данных с сайта [minerals.net](https://www.minerals.net): создание каталогов с названием другоценных камней и сохранение изображений в соответствующие каталоги.  

1. Страница [list of all gemstones](https://www.minerals.net/GemStoneMain.aspx) содержит таблицу со списком камней:
```python
page = 'https://www.minerals.net/GemStoneMain.aspx'
resp = requests.get(page)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        table_gems=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```
3. Считать ссылки на страницы к каждому драгоценному камню и создать словарь `{gemstone name : link }`.

4. Распарсить каждую страницу и получить изображения.
```python
table_images=soup.find_all('table',{'id':'ctl00_ContentPlaceHolder1_DataList1'})
```

## [Парсинг Habr Career](https://github.com/LSIND/advanced-python3/tree/master/HabrCareer)
> BeautifulSoup + dynamic content       
> Cобирает информацию о вакансиях с сайта Habr Career и представляет её в виде объектов класса.

1. Принимает поисковый запрос (например, "аналитик")
2. Отправляет GET-запрос к https://career.habr.com/vacancies?q={запрос} 
3. Парсит HTML-страницу с помощью BeautifulSoup
4. Извлекает информацию по каждой вакансии
5. Создаёт экземпляры класса Vacancy и помещает их в список

## [Gismeteo Web Scraping + SQLAlchemy](https://github.com/LSIND/advanced-python3/tree/master/GismeteoSqlAlchemy)
> BeautifulSoup + SQLite       
> Получение данных из [gismeteo.ru](https://www.gismeteo.ru): город + период. Сохранение данных в БД с помощью ORM sqlalchemy v2

1. Установка пакетов:  
```Console
pip install beautifulsoup4
pip install sqlalchemy
```
1. Пример страницы: [погода в Москве за последние 14 дней](https://www.gismeteo.ru/weather-moscow-4368/2-weeks/). HTML-элемент класса `widget-items`.
2. Выгрузить день недели, дату, описание, температуру (max), температуру (min), скорость ветра (м/с), направление ветра, осадки, влажность, уровень радиации.
3. Создать класс Weather с соответствующими полями.
4. Создать SqlAlchemy Engine (подключение), SqlAlchemy Table с 10 столбцами и mapper между классом Weather и SqlAlchemy Table.
5. Обработать данные с сайта так, чтобы получить строку, дату, число с плавающей запятой и т.д. Вставить данные в БД. Учесть возможное дублирование данных.

## [Python + MongoDB](https://github.com/LSIND/advanced-python3/tree/master/MongoDbProvider)
> Работа с nosql базой данных с помощью python.   
> Базовые операции при работе с MongoDB с помощью модуля pymongo.  
> *opt: скачать и установить GUI [Compass](https://www.mongodb.com/products/compass)*
```Console
pip install pymongo
```
База данных примера: [weather.json](https://atlas-data-lake.s3.amazonaws.com/json/sample_weatherdata/data.json). Импортировать данные в экземпляр MongoDB и изучить коллекцию документов: **Schema -> Analyze**.  

Проверить запросы с помощью mongosh/Compass:  
```Console
{"airTemperature.value": 3}
{"airTemperature.value": {$gt: 10}}
{"wind.type": {$ne: "N"}}
{"atmosphericPressureChange" : {$exists: true}}
```

1. Реализовать CRUD операции к MongoDB с помощью pymongo: ```insert_one (insert_many), find, update_one (update_many), delete_one (delete_many)```. Данные функции принимают на вход словарь/словари в качестве параметров.