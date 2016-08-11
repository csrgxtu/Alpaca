#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: DownloadTagedSpineImage.py
# Desc: 下载被标记的book spine image
# Date: 11/Aug/2016
# Produced By BR
from pymongo import MongoClient
import unirest

client = MongoClient('mongodb://linyy:rioreader@192.168.200.22:27017/bookshelf')
db = client['bookshelf']
sc = db['spinetmp']

# foreach document, get isbn and img link
imgs = sc.find({'isbn': {'$exists': True}})
for img in imgs:
    try:
        filename = img['isbn'] + '-' + img['url'].split('/')[-1]
        unirest.timeout(20)
        response = unirest.get(img['url'])
        with open('../data/img/' + filename, 'w') as F:
            F.write(response.body)

        print img['isbn'], img['url']
    except:
        print 'Error: ', img['_id']
