#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer
# File: ExtractFeatureToMongo.py
# Desc: 提取图片特征并且存入到ｍｏｎｇｏ数据库
# Date: 13/Aug/2016
#
# Produced By BR
from pymongo import MongoClient
from ImgFeatureExtractor import ImgFeatureExtractor
import pickle

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['Alpaca']
fc = db['feature']

# for each image, load feature, pickle it, save it to db
Images = []
with open('../data/images.txt', 'r') as F:
    for line in F:
        Images.append('../data/img/' + line.strip('\n'))

FeatureMat = []
for img in Images:
    print img
    tmp = []
    I = ImgFeatureExtractor(img)
    kp, des = I.SURF()
    tmp.append(img.split('-')[0].split('/')[-1]) #isbn
    tmp.append(img) # filename
    # tmp.append(pickle.dumps(kp)) #keypoints
    tmp.append(pickle.dumps(des)) #descriptions

    FeatureMat.append(tmp)

for f in FeatureMat:
    data = {
        "isbn": f[0],
        "filename": f[1],
        "des": f[2]
    }
    print fc.insert_one(data).inserted_id