#!/usr/bin/env python

import uuid
import ConfigParser
import pymongo
import json
import requests
import sys, os
from os.path import isdir, join


class StatusWriter():
  mongo_client = pymongo.MongoClient()
  db = mongo_client['eumssi_test']
  col = db['content_items']

  def write_status(self, item, source):
    ''' write video meta to Mongodb '''
    try:
      twuid = uuid.uuid4()
      print "inserted: ", self.col.insert({'_id':uuid.uuid4(),'source': source,'meta':{'original':item, 'original_format':'eumssi-crawler-v102014'}})
    except Exception as e:
      print e

'''
Extract items and insert to DB
'''
def readJsonData(_param_data_file, source):    
    fi = open (_param_data_file, 'r')  
    #parse that file
    jsoncontent = fi.read()
    itemset = json.loads(jsoncontent)
    #get items
    print "Infor: ", len(itemset), " news articles found"
    #write data to mongo db
    writer = StatusWriter()   
    i = 0
    for item in itemset:
        i+=1
        print i, " item indexed "
        writer.write_status(item, source)

if __name__ == '__main__':
  _param_data_file = "/Work/EUMSSI/data/news/fracking_news_nov.json"
  source = "Eumssi-News-Crawler"
  readJsonData(_param_data_file, source)