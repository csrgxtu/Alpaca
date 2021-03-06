#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: DownloadTagedSpineImage.py
# Desc: 下载被标记的book spine image
# Date: 11/Aug/2016
# Produced By BR
from pymongo import MongoClient
from qiniu import Auth
import unirest

client = MongoClient('mongodb://192.168.200.22:27017/bookshelf')
db = client['bookshelf']
sc = db['spinetmp']

access_key = ''
secret_key = ''
q = Auth(access_key, secret_key)
# private_url = q.private_download_url(base_url, expires=3600)

# foreach document, get isbn and img link
imgs = sc.find({'isbn': {'$exists': True, '$ne': ''}}, no_cursor_timeout = True)
for img in imgs:
    try:
        filename = img['isbn'] + '-' + img['url'].split('/')[-1]
        unirest.timeout(20)
        response = unirest.get(q.private_download_url(img['url'], expires=3600))
        with open('../data/img/' + filename, 'w') as F:
            F.write(response.body)

        print img['isbn'], img['url']
    except:
        print 'Error: ', img['_id']
