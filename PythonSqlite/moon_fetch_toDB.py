#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Fetch data from fullmoon.info and put in sqlite3 db'''

import requests
from bs4 import BeautifulSoup as bs
from datetime import date
from create_sqlitedb import *

url = 'https://www.fullmoon.info/en/fullmoon-calendar/'
YEAR = date.today().year # page with present year is different
global conn

def get_phases(years):
    '''takes a list of years in specified range and returns a list of strings: full moons for every year'''
    all_moons = []
    for i in years:
        print('--'*10)
        if(i != YEAR):
            html = requests.get(url+str(i)).text
            print(url + str(i))
            soup = bs(html, 'html.parser')
            selector = 'tr span'
            rows = soup.select(selector)
            rows[12].find('i').extract()        # extract unwanted element <i>
            q = rows[12].text
            q = q.replace('\t', '').replace('    ', '').strip()

        else:      # current year
            html = requests.get(url[:-1]+'.html').text
            print(url)
            soup = bs(html, 'html.parser')
            for br in soup.find_all('br'):
                br.replace_with('\n')
            selector = 'div p'
            rows = soup.select(selector)
            q = rows[3].text.replace('\n ', '\n')

        insert_moons(q)


def insert_moons(row):
    t = []
    year_list = row.split('\n')
    for y in year_list:
        li = y.split(', ')
        li = tuple(li)
        print(li)
        t.append(li)
    conn.executemany("INSERT INTO FullMoon(weekday, date, time) VALUES (?,?,?)", t)
    conn.commit()



if __name__ == '__main__':
    db = 'fullmoon.db'
    create_fullmoon_table = """ CREATE TABLE IF NOT EXISTS FullMoon (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        weekday text NOT NULL,
                                        date text,
                                        time text
                                    ); """
    conn = create_connection(db)
    
        # create tables
    if conn is not None:
        create_table(conn, create_fullmoon_table)
        y = list(range(1900, 2051))
        get_phases(y)
    else:
        print("Error! cannot create the database connection.")


