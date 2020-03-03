#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker
from Weather import Weather


class AlchContext:
    def __init__(self, provider):               #dbcontext
        AlchContext.Engine = create_engine(provider)
        metadata = MetaData()
        
        AlchContext.w_table = Table('weatherMoscow', metadata,
            Column('id', Integer, primary_key=True),
            Column('day', String),
            Column('date', String),
            Column('desc', String),
            Column('temp', Integer),
            Column('precip', String),
            Column('wind', String),
            Column('humidity', Integer)
        )
        metadata.create_all(AlchContext.Engine)
        mapper(Weather, AlchContext.w_table)


    def alchemy_commit(self, Class):
        Session = sessionmaker(bind=AlchContext.Engine)
        AlchContext.session = Session()
        
        try:
            for w in Class.list_objects:
                AlchContext.session.add(w)
            print(Class.list_objects)
            AlchContext.session.commit()
        except:
            AlchContext.session.rollback()
            print('error')
        finally:
            AlchContext.session.close()

    def select_data(self):
        for instance in AlchContext.session.query(AlchContext.w_table).order_by(Weather.humidity): 
            print(instance)