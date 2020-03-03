#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mongo_context
import datetime

if __name__ == '__main__':
    srv = 'mongodb://127.0.0.1:27017'
    mongo_context.create_client(srv)
    
    #select
    mongo_context.select_data("qualityControlProcess", "V020",5)

    #update
    mongo_context.update_data({'callLetters':'TFBY'}, {'qualityControlProcess' : 'TEST TEST'})
    
    
    #delete
    mongo_context.delete_data({'qualityControlProcess' : 'TEST TEST'})
    
    #insert
    doc = {'st': 'x+60900-005300', 'ts': datetime.datetime(1984, 3, 5, 15, 0), 'position': {'type': 'Point', 'coordinates': [-5.3, 60.9]}, 'elevation': 9999, 'callLetters': 'TFRB', 'qualityControlProcess': 'V020', 'dataSource': '4', 'type': 'FM-13', 'airTemperature': {'value': 7.5, 'quality': '1'}, 'dewPoint': {'value': 999.9, 'quality': '9'}, 'pressure': {'value': 1018.5, 'quality': '1'}, 'wind': {'direction': {'angle': 220, 'quality': '1'}, 'type': 'N', 'speed': {'rate': 12.3, 'quality': '1'}}, 'visibility': {'distance': {'value': 4000, 'quality': '1'}, 'variability': {'value': 'N', 'quality': '9'}}, 'skyCondition': {'ceilingHeight': {'value': 99999, 'quality': '9', 'determination': '9'}, 'cavok': 'N'}, 'sections': ['AG1', 'AY1', 'GF1', 'MW1'], 'precipitationEstimatedObservation': {'discrepancy': '2', 'estimatedWaterDepth': 0}, 'pastWeatherObservationManual': [{'atmosphericCondition': {'value': '0', 'quality': '1'}, 'period': {'value': 3, 'quality': '1'}}], 'skyConditionObservation': {'totalCoverage': {'value': '08', 'opaque': '99', 'quality': '1'}, 'lowestCloudCoverage': {'value': '99', 'quality': '9'}, 'lowCloudGenus': {'value': '99', 'quality': '9'}, 'lowestCloudBaseHeight': {'value': 99999, 'quality': '9'}, 'midCloudGenus': {'value': '99', 'quality': '9'}, 'highCloudGenus': {'value': '99', 'quality': '9'}}, 'presentWeatherObservationManual': [{'condition': '02', 'quality': '1'}]}
    mongo_context.insertone_data(doc)
