#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker  # v 2.0
from Weather import Weather

class WeatherRepository:

    def __init__(self, context):
        self.__repo = context
        Session = sessionmaker(bind = self.__repo.Engine)
        self.__repo.session = Session()

    def create_object(self, obj):        
        if obj is None:    # and other checkings
            return
        if type(obj) is not Weather:
            return
        if obj.date is None:
            return

        try:
            # do not insert existing items (by date)
            dupl = self.__repo.session.query(self.__repo.w_table).filter(Weather.date == obj.date).first()
            if dupl is None:
                self.__repo.session.add(obj)
                self.__repo.session.commit()
        except Exception as e:
            self.__repo.session.rollback()
            print('error')
            print(e)
        #finally:
            #self.__repo.session.close()
            #self.__repo.Engine.dispose()

    def select_data(self):
        for instance in self.__repo.session.query(self.__repo.w_table): #.order_by(Weather.tempMax.desc()): 
            print(instance)