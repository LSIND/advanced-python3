#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
import os, locale
import requests
from bs4 import BeautifulSoup
from AlchContext import AlchContext
from Weather import Weather
from WeatherRepository import WeatherRepository

def get_data(link, days_count = 14):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content = requests.get(link, headers = headers)
    
    if content.status_code == 200:
        content = content.text        
        soup = BeautifulSoup(content, 'html.parser')

        table_info = soup.find('div', {'class': 'widget-items'})
        humidity_info = soup.find('div',{'data-row':'humidity'})
        radiation_info = soup.find('div',{'data-row':'radiation'})

        days=table_info.find_all('div',{'class':'day'})                         # день недели
        dates=table_info.find_all('div',{'class':'date'})                       # дата
        desc=table_info.find_all('div', { 'class': "weather-icon tooltip" })    #.get('data-text') # описание иконки
        tempMax = table_info.find_all('div',{'class':'maxt'})                   # макс темп.
        tempMin = table_info.find_all('div',{'class':'mint'})                   # мин темп.
        winds=table_info.find_all('span',{'class':'wind-unit unit unit_wind_m_s'}) # порывы ветра в м\с
        wind_direction = table_info.find_all('div',{'class':'direction'})       # направление ветра
        precip=table_info.find_all('div',{'class':'item-unit'})                 # осадки мм        
        humidity = humidity_info.find_all('div',{'class':'row-item'})           # отн.влажность
        radiation = radiation_info.find_all('div',{'class':'row-item'})         # УФ - индекс

        YEAR = date.today().year
        locale.setlocale(locale.LC_ALL, 'ru_RU')  # для преобразования дат
        startdate = date.today()

        for i in range(0, days_count):
            try:
                wday = days[i].text                 # char(2)
                dt = dates[i].text                  # need cast to date
                if i == 0 or len(dt) > 3:
                     firstdate = datetime.strptime(dt, '%d %B')   # 24 Май
                     startdate = firstdate.replace(year = YEAR).date()
                elif dt.isdigit():
                    new_date = startdate + timedelta(days=1)
                    if int(dt) == new_date.day:
                        startdate += timedelta(days=1)
                else:
                    startdate += timedelta(days=1)

                descr = desc[i].get('data-text')    # varchar
                tMax = int(tempMax[i].find('span', {'class':'unit unit_temperature_c'}).text.replace('−','-'))  # int
                tMin = int(tempMin[i].find('span', {'class':'unit unit_temperature_c'}).text.replace('−','-'))  # int
                prec = float(precip[i].text.replace(',','.'))     # numeric
                wind_dir = wind_direction[i].text   # char(2)
                wind = int(winds[i].text)           # int
                hum = int(humidity[i].text)         # int
                rad = int(radiation[i].text)        # int


                w = Weather(wday, startdate, descr, tMax, tMin, wind, wind_dir, prec, hum, rad) # object model
                print(wday, startdate, descr, tMax, tMin, wind, wind_dir, prec, hum, rad, sep = ' | ')

            except Exception as e:
                print (e)
        #return Weather.list_objects
        print('Done')
        return Weather.list_objects

    else:
        print(f'Connection refused: {content.status_code}')

if __name__ == '__main__':
    #context = AlchContext('sqlite:///weather.db')
    dbpath = os.path.join(os.path.dirname(__file__), 'weather.db')
    context = AlchContext(f'sqlite:///{dbpath}')
    w_repo = WeatherRepository(context)
    gismeteo_link = 'https://www.gismeteo.ru/weather-moscow-4368/2-weeks/'
    data = get_data(gismeteo_link)   # получение данных

    if data:
        # create db connection
        for o in data:
            w_repo.create_object(o)
        w_repo.select_data()