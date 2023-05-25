#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''''class Weather (Model)'''

class Weather:
    list_objects = []
    def __init__(self, wday, date, desc, tMax, tMin, wind, winddir, precip, humidity, rad):
        self.wday = wday
        self.date = date
        self.description = desc
        self.tempMax = tMax
        self.tempMin = tMin        
        self.wind = wind
        self.winddir = winddir
        self.precip = precip
        self.humidity = humidity
        self.radiation = rad
        type(self).list_objects.append(self)