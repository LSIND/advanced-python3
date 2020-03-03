#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

wcol = None

def create_client(srv):
    '''dbcontext'''
    try:
        global wcol
        client = MongoClient(srv)
        wcol = client.weatherDB.weather
        print('connection created')
        print('collection weather connected; docs:', wcol.count_documents({}))
    except Exception as e:
        print(e)

    
def select_data(field, val, limit=100):
    '''find method example on FIELD, VAL with LIM'''
    print('query', field, '=', val)
    print(wcol)
    c1 = wcol.find( { field: val}  ).limit(limit)
    for c in c1:
        print(c)


def insertone_data(doc):
    '''insert_one example, doc = {} - dictionary'''
    try:
        wcol.insert_one(doc)
    except Exception as e:
        print(e)

def update_data(search, changeddata):
    '''update_many search = {'field' : 'val'} - dict, changeddata = {'field' : 'val'} - dict'''
    try:
        wcol.update_many( search, {'$set': changeddata}  )
        c6 = wcol.find(search)
        for c in c6:
            print(c)
    except Exception as e:
        print(e)

def delete_data(search):
    '''delete_many search = {'field' : 'val'} - dict'''
    try:
        d = wcol.delete_many(search)
        print(d.deleted_count)
    except Exception as e:
        print(e)
