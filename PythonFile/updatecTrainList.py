# _*_ coding: utf-8 _*_

import ticket
import cons
import re

cons.getStationName()
config = cons.readConfig()
fromCity = config['出发地']
toCity = config['目的地']
trainDate = config['刷新日期']
if len(fromCity) > 0 and len(toCity) > 0 and len(trainDate) > 0:
    trainDate = trainDate.split(',')[0]
    try:
        list = ticket.getTrainRquestList(fromCity, toCity, trainDate)
        print(len(list))
        print(cons.trainListPath)
        cons.saveData(cons.trainListPath, list)
    except ZeroDivisionError as e:
        print('except:',e)
    finally:
        print('finally')



