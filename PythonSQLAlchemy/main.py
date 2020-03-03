#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
from Weather import Weather
from AlchContext import AlchContext


def get_data(link):
    content = requests.get(link).text
    soup = bs(content, 'html.parser')

    all=soup.find('div',{'class':'locations-title ten-day-page-title'}).find('h1').text
    table=soup.find_all('table',{'class':'twc-table'})
    for items in table:
        for i in range(len(items.find_all('tr'))-1):

            day=items.find_all('span',{'class':'date-time'})[i].text
            date=items.find_all('span',{'class':'day-detail'})[i].text
            desc=items.find_all('td',{'class':'description'})[i].text 
            temp=items.find_all('td',{'class':'temp'})[i].text 
            precip=items.find_all('td',{'class':'precip'})[i].text.replace('%', '')
            wind=items.find_all('td',{'class':'wind'})[i].text  
            humidity=items.find_all('td',{'class':'humidity'})[i].text.replace('%', '') 
            w = Weather(day, date, desc, temp, precip, wind, humidity)
    #print(Weather.list_objects)


if __name__ == '__main__':
    context = AlchContext('sqlite:///alc.db')
    get_data('https://weather.com/en-IN/weather/tenday/l/34f2aafc84cff75ae0b014754856ea5e7f8ddf618cf9735549dfb5e016c28e10')
    
    context.alchemy_commit(Weather)
    context.select_data()
