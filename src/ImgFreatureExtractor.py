#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer
# File: ImgFeatureExtractor.py
# Desc: 提取各种图片的特征
# Date: 13/Aug/2016
#
# Produced By BR
import cv2

class ImgFeatureExtractor(object):
    FileName = None
    Img = None

    def __init__(self, filename):
        self.FileName = filename
        self.Img = cv2.imread(self.FileName)

    def SURF(self, HessianThreshold=400):
        surf = cv2.SURF(HessianThreshold)
        kp, des = surf.detectAndCompute(self.Img, None)
        return kp, des

    def SIFT(self, HessianThreshold=400):
        pass
