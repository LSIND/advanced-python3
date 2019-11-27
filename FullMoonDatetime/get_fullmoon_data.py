#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Fetch data from fullmoon.info'''

import requests
from bs4 import BeautifulSoup as bs
from datetime import date

url = 'https://www.fullmoon.info/en/fullmoon-calendar/'
YEAR = date.today().year # page with present year is different

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

        print(q)
        all_moons.append(q)
    return all_moons

if __name__ == '__main__':
    y = list(range(1900, 2051))
    all_data = get_phases(y)
    with open('full_moon.txt', 'a+') as f:
        for item in all_data:
            f.write("%s\n" % item)
