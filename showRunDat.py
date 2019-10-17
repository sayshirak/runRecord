#-*- coding: UTF-8 -*-
__author__ = 'gy'

import os
import time
import numpy as np
import pandas as pd
import getRunDat
from pyecharts.charts import Line,Page
from pyecharts import options as opts

from pyecharts.faker import Collector, Faker

C = Collector()
listDate = []
listDistance = []
listTime = []
listPace = []
listCal = []
listHeartRate = []
listStepFrequency = []
listStride = []
countMon = []
DistanceMon = []
countYear = []
DistanceYear = []

def datPrepare():
    rawDat = getRunDat.getRunDat()
    height = rawDat.shape[0]
    for row in range(height-1):
        listDate.append(rawDat.iloc[row, 0])
        if( np.isnan(rawDat.iloc[row, 1]) ):
            break
        listDistance.append(rawDat.iloc[row, 1])
        listTime.append("0000-00-00 " + rawDat.iloc[row, 2])
        listPace.append("0000-00-00 " + rawDat.iloc[row, 3])
        listCal.append(rawDat.iloc[row, 4])
        listHeartRate.append(rawDat.iloc[row, 5])
        listStepFrequency.append(rawDat.iloc[row, 6])
        listStride.append(rawDat.iloc[row, 7])
        countMon.append(rawDat.iloc[row, 8])
        DistanceMon.append(rawDat.iloc[row, 9])
        countYear.append(rawDat.iloc[row, 10])
        DistanceYear.append(rawDat.iloc[row, 11])

@C.funcs
def showDatDistance() -> Line:
    C = (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                    name="日期",
                    #splitline_opts=opts.SplitLineOpts(is_show=True),
                    is_scale=True
                ))
                .add_yaxis("跑步距离",listDistance).set_global_opts(
                            yaxis_opts=opts.AxisOpts(
                                type_="value",
                                is_scale=True
                            ),
                            title_opts=opts.TitleOpts(title="跑步距离曲线")
        )
    )
    #lineDist.render("dateDistance.html")
    return C

@C.funcs
def showDatTime() -> Line:
    C= (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                    name="日期",
                    #splitline_opts=opts.SplitLineOpts(is_show=True),
                    is_scale=True
                ))
                .add_yaxis("跑步时间",listTime).set_global_opts(
                            yaxis_opts=opts.AxisOpts(
                                type_="time",
                                is_scale=True
                            ),
                            title_opts=opts.TitleOpts(title="跑步时间曲线")
        )
    )
    #lineTime.render("dateTime.html")
    return C

@C.funcs
def showDatPace() -> Line:
    C = (
        Line()
            .add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                name="日期",
                #splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True
            ))
            .add_yaxis("每公里配速",listPace).set_global_opts(
                        yaxis_opts=opts.AxisOpts(
                            type_="time",
                            is_scale=True
                        ),
                        title_opts=opts.TitleOpts(title="配速曲线")
        )
    )
    #linePace.render("paceTime.html")
    return C

@C.funcs
def showDatCal() -> Line:
    C = (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                name="日期",
                #splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True
            ))
            .add_yaxis("消耗能量",listCal).set_global_opts(
                        yaxis_opts=opts.AxisOpts(
                            type_="value",
                            is_scale=True,
                        ),
                        title_opts=opts.TitleOpts(title="能耗曲线")
        )
    )
    #lineCal.render("calConsum.html")
    return C

@C.funcs
def showDatHeartRate() -> Line:
    C = (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                name="日期",
                #splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True
            ))
            .add_yaxis("平均心率",listHeartRate).set_global_opts(
                        yaxis_opts=opts.AxisOpts(
                            type_="value",
                            is_scale=True,
                        ),
                        title_opts=opts.TitleOpts(title="心率曲线")
        )
    )
    #lineHeartRate.render("heartRate.html")
    return C

@C.funcs
def showDatFrequency() -> Line:
    C = (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                name="日期",
                #splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True
            ))
            .add_yaxis("平均步频",listStepFrequency).set_global_opts(
                        yaxis_opts=opts.AxisOpts(
                            type_="value",
                            is_scale=True,
                        ),
                        title_opts=opts.TitleOpts(title="步频曲线")
        )
    )
    #lineStepFrequency.render("stepFrequency.html")
    return C

@C.funcs
def showDatStride() -> Line:
    C = (
        Line().add_xaxis(listDate).set_global_opts(xaxis_opts=opts.AxisOpts(
                name="日期",
                #splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True
            ))
            .add_yaxis("平均步幅",listStride).set_global_opts(
                        yaxis_opts=opts.AxisOpts(
                            type_="value",
                            is_scale=True,
                        ),
                        title_opts=opts.TitleOpts(title="步幅曲线")
        )
    )
    #lineStride.render("stepStride.html")
    return C


if __name__ == '__main__':
    time1 = time.time()
    print(time1)
    datPrepare()
    Page().add(*[fn() for fn, _ in C.charts]).render("runDat.html")
    time2 = time.time()
    print(time2)