#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, Float, String, Date, MetaData
from sqlalchemy.orm import registry
from Weather import Weather

class AlchContext:
    def __init__(self, provider):               #dbcontext
        AlchContext.Engine = create_engine(provider)
        metadata = MetaData()
        
        AlchContext.w_table = Table('weather', metadata,
            Column('id', Integer, primary_key=True),
            Column('wday', String(3)),
            Column('date', Date),
            Column('description', String(100)),            
            Column('tempMax', Integer),
            Column('tempMin', Integer),
            Column('wind', Integer),
            Column('winddir', String(3)),
            Column('precip', Float),            
            Column('humidity', Integer),
            Column('radiation', Integer)
        )
        metadata.create_all(AlchContext.Engine)
        mapper_reg = registry() # 2.0
        mapper_reg.map_imperatively(Weather, AlchContext.w_table)