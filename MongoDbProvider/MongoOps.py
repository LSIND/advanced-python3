#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoOps:
    wcol = None
    
    def __init__(self, srv, db, coll): #dbcontext
        client = MongoClient(srv, serverSelectionTimeoutMS = 5000)
        try:
            client.admin.command('ping')
            if db in client.list_database_names(): # check if dbs and collection exist
                db_name = client.get_database(db)
                if coll in db_name.list_collection_names():
                    type(self).wcol = client.get_database(db).get_collection(coll)
                else:
                    raise SourceException(coll)
            else:
                raise SourceException(db)
        
        except Exception as e:
            self.connected = False
            print(f'Connection failure. {e}')
            client.close()
        else:
            self.connected = True
            print('Connection created')
            print(f'collection {coll} connected; docs:', type(self).wcol.count_documents({}))
            

    def select_data(self, filt, projection = {}, limit = 0):
        if type(self).wcol is not None:
            print(filt)
            c1 = type(self).wcol.find( filt, projection ).limit(limit)
            for c in c1:
                print(c)

    def insertone_data(self, doc):
        if type(self).wcol is not None:
            try:
                type(self).wcol.insert_one(doc)
                return 1
            except Exception as e:
                print(e)
                return None

    def update_data(self, filt, new_data):
        if type(self).wcol is not None:
            try:
                u = type(self).wcol.update_many( filt, {'$set': new_data}  )
                return u.modified_count
            except Exception as e:
                print(e)
                return None

    def delete_data(self, filt):
        if type(self).wcol is not None:
            try:
                d = type(self).wcol.delete_many(filt)
                return d.deleted_count
            except Exception as e:
                print(e)
                return None

class SourceException(Exception):
    '''Error conencting to source.
        source - db or collection
        message - error message
    '''
    def __init__(self, source, message='No such source'):
        self.source = source
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.source}: {self.message}'