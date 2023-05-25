#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Fetch data from fullmoon.info.
Changed 2023'''

from datetime import datetime
import csv, os, sqlite3
import requests
from bs4 import BeautifulSoup

def write_to_csv(list_of_tuples, path_file):
    path_file = os.path.join(os.path.dirname(__file__), path_file)
    try:
        with open(path_file, 'a+', newline='') as csvfile: 
            writer = csv.writer(csvfile)
            #writer.writerow(['dow', 'date', 'time'])  # header
            for tup in list_of_tuples:
                writer.writerow(tup)
    except Exception as e:
        print(f'error {e}')
        return 'error write to csv.'
    else:
        return 'Done to csv.'

def get_year(year, page):
    '''takes a list of years in specified range and returns a list of strings: full moons for every year''' 
    resp = requests.get(page)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        t = soup.find('table', {'class':'table-calendar'})
        #t.find('td', {'class': 'notes'}).extract() # extract inplace
        all_moons = []
        for x in t.find_all('td'):
            if x.attrs != {'class': ['notes']}:   # all except notes
                all_moons.append(x.text)
                
        if all_moons is not None:
            all_moons = [x for x in zip(*[iter(all_moons)]*3)] # tuples ('Sunday', '15 April 1900', '02:02:06 am')
            print(year, write_to_csv(all_moons, 'fullmoons.txt'))  # write to csv

            list_todb = [] # tuples ('Sunday', 'datetime')
            for tup in all_moons:
                
                try:
                    dt = datetime.strptime(tup[1]+ tup[2][:11], '%d %B %Y%I:%M:%S %p')
                except:
                    dt = None
                    print('invalid row: ', tup)
                else:
                    #print(tup[0], dt) # tuples ('Sunday', 'datetime')
                    if dt is not None and tup[0] is not None:
                        list_todb.append((tup[0], dt))
            return list_todb
        else:
            print(f'{year} : skip')
    else:
        print(f'status code {resp.status_code}')
    return all_moons

if __name__ == '__main__':
    url = 'https://www.fullmoon.info/en/fullmoon-calendar/'
    years = range(1900, 2051) # 150 years

    db = 'newdb.db'
    path_db = os.path.join(os.path.dirname(__file__), db)
    print(path_db)
    table_q = '''DROP TABLE IF EXISTS Phases;
                 CREATE TABLE Phases (id integer primary key autoincrement, 
                 weekday text not null, date datetime);'''
    conn = sqlite3.connect(path_db)
    
    c = conn.cursor()
    c.executescript(table_q)
    conn.commit()

    for y in years:
        p = f'{url}{y}.html'
        print(p)
        year_data = get_year(y, p)  # N year data ready to write to database

        if year_data is not None:
            conn.executemany('INSERT INTO Phases(weekday, date) VALUES (?,?);', year_data)
            conn.commit()
            print(f'{y} Done to database.')
        
        print('--'*10)
    
    conn.close()