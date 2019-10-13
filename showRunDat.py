#-*- coding: UTF-8 -*-
__author__ = 'gy'

import os
import time
import numpy as np
import pandas as pd
import getRunDat
from pyecharts.charts import Line,Page
from pyecharts import options as opts

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
        listDate.append(rawDat.iloc[row, 0])
        if( np.isnan(rawDat.iloc[row, 1]) ):
            break
        listDistance.append(rawDat.iloc[row, 1])
        listTime.append(rawDat.iloc[row, 2])
        listPace.append(rawDat.iloc[row, 3])
        listCal.append(rawDat.iloc[row, 4])
        listHeartRate.append(rawDat.iloc[row, 5])
        listStepFrequency.append(rawDat.iloc[row, 6])
        listStride.append(rawDat.iloc[row, 7])
        countMon.append(rawDat.iloc[row, 8])
        DistanceMon.append(rawDat.iloc[row, 9])
        countYear.append(rawDat.iloc[row, 10])
        DistanceYear.append(rawDat.iloc[row, 11])
    lineDist = Line()
    lineDist.add_xaxis(listDate)
    lineDist.add_yaxis("跑步距离",listDistance)
    lineDist.set_global_opts(title_opts=opts.TitleOpts(title="跑步距离曲线"))
    lineDist.render("dateDistance.html")

    lineTime = Line()
    lineTime.add_xaxis(listDate)
    lineTime.add_yaxis("跑步时间",listTime).set_global_opts(yaxis_opts=opts.AxisOpts(
                type_="time",
                name="跑步时间",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,
            ))

    lineTime.set_global_opts(title_opts=opts.TitleOpts(title="跑步时间曲线"))
    lineTime.render("dateTime.html")


if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    showDat()
    time2 = time.time()
    print(time2)