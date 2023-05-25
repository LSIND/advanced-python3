#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from MongoOps import MongoOps

if __name__ == '__main__':
    srv = 'mongodb://127.0.0.1:27017'
    mng = MongoOps(srv, 'weather', 'weatherSeries') # server, DB, Collection
    if(mng.connected):
        #select
        print(20*'-')
        filter1 = {'qualityControlProcess': 'V020'}
        project1 = {'st':1, 'airTemperature': 1, 'position': 1}
        mng.select_data(filter1, project1, 5)
        
        #update
        print(20*'-')
        filterUpd = {'callLetters':'TFBY'}
        newValue = {'qualityControlProcess' : 'TEST TEST'}
        upCount = mng.update_data(filterUpd, newValue)
        print(f'Updated: {upCount} documents')
        
        #delete
        print(20*'-')
        filterDel = {'qualityControlProcess' : 'TEST TEST'}
        delCount = mng.delete_data(filterDel)
        print(f'Deleted: {delCount} documents')
        
        #insert_one
        doc = {'st': 'x+60900-005300', 'ts': datetime.datetime(1984, 3, 5, 15, 0), 'position': {'type': 'Point', 'coordinates': [-5.3, 60.9]}, 'elevation': 9999, 'callLetters': 'TFRB', 'qualityControlProcess': 'V020', 'dataSource': '4', 'type': 'FM-13', 'airTemperature': {'value': 7.5, 'quality': '1'}, 'dewPoint': {'value': 999.9, 'quality': '9'}, 'pressure': {'value': 1018.5, 'quality': '1'}, 'wind': {'direction': {'angle': 220, 'quality': '1'}, 'type': 'N', 'speed': {'rate': 12.3, 'quality': '1'}}, 'visibility': {'distance': {'value': 4000, 'quality': '1'}, 'variability': {'value': 'N', 'quality': '9'}}, 'skyCondition': {'ceilingHeight': {'value': 99999, 'quality': '9', 'determination': '9'}, 'cavok': 'N'}, 'sections': ['AG1', 'AY1', 'GF1', 'MW1'], 'precipitationEstimatedObservation': {'discrepancy': '2', 'estimatedWaterDepth': 0}, 'pastWeatherObservationManual': [{'atmosphericCondition': {'value': '0', 'quality': '1'}, 'period': {'value': 3, 'quality': '1'}}], 'skyConditionObservation': {'totalCoverage': {'value': '08', 'opaque': '99', 'quality': '1'}, 'lowestCloudCoverage': {'value': '99', 'quality': '9'}, 'lowCloudGenus': {'value': '99', 'quality': '9'}, 'lowestCloudBaseHeight': {'value': 99999, 'quality': '9'}, 'midCloudGenus': {'value': '99', 'quality': '9'}, 'highCloudGenus': {'value': '99', 'quality': '9'}}, 'presentWeatherObservationManual': [{'condition': '02', 'quality': '1'}]}
        mng.insertone_data(doc)
    else:
        print('Connection error')