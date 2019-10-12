#-*- coding: UTF-8 -*-
__author__ = 'gy'

import os
import time
import numpy as np
import pandas as pd
import getRunDat

def showDat():
    rawDat = getRunDat.getRunDat()
    height = rawDat.shape[0]
    listDate = []
    listDistance = []
    listTime = []
    listPace= []
    listCal = []
    listHeartRate = []
    listStepFrequency = []
    listStride = []
    countMon = []
    DistanceMon = []
    countYear = []
    DistanceYear = []
    for row in range(height-1):
        listDate.append(rawDat.iloc[row,0])

if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    showDat()
    time2 = time.time()
    print(time2)