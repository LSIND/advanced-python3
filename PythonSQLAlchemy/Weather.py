#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Weather:
    list_objects = []
    def __init__(self, day, date, desc, temp, precip, wind, humidity):
        self.day = day
        self.date = date
        self.desc = desc
        self.temp = temp
        self.precip = precip
        self.wind = wind
        self.humidity = humidity
        type(self).list_objects.append(self)

    def __repr__(self):
        return "<Weather('%s','%s', '%s','%s','%s','%s','%s')>" % (self.day, self.date, self.desc, self.temp, self.precip, self.wind, self.humidity)