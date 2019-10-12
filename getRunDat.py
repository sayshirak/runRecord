#-*- coding: UTF-8 -*-
__author__ = 'gy'

import os
import time
import numpy as np
import pandas as pd

def getRunDat():
    data_original = pd.read_csv('runRecord.csv', encoding = 'gb2312')
    height = data_original.shape[0]
    width = 12

if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    getRunDat()
    time2 = time.time()
    print(time2)