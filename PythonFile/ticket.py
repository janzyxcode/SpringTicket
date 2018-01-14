# _*_ coding: utf-8 _*_

import re
import cons
import login
import ngRequest
import json


# 同时再结合登录,购票等流程,通过自动判断是否有票,如果无票就继续刷新,直到有票之后自动登录下单后通过短信或者电话等方式全自动联系购票人手机就可以

# 联众-收费

# https://www.itsvse.com/thread-4113-1-1.html


def getTrainRquestList(fromCity, toCity, trainDate):
    startCityCode = cons.getCityCodeWithName(fromCity)
    endCityCode = cons.getCityCodeWithName(toCity)
    urlStr = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + trainDate + '&leftTicketDTO.from_station=' + startCityCode + '&leftTicketDTO.to_station=' + endCityCode + '&purpose_codes=ADULT'
    print(urlStr)
    response = ngRequest.getRequest(urlStr)
    # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    trainDictList = []
    if response.status_code == 200:
        dic = response.json()
        # print(dic)
        result = dic['data']['result']
        # print(result)
        trainDictList = decoTrainResponse(result)
    return trainDictList


def decoTrainResponse(result):
    trainDictList = []
    print('train list len ', len(result))
    for item in result:
        ti = item.split('|')
        # print(item)
        dict = {}
        dict["状态"] = ti[1]
        # dict[""] = ti[2]
        dict["车次"] = ti[3]
        # dict["4"] = ti[4]
        # dict["5"] = ti[5]
        dict["始发站"] = cons.getCityNameWithCode(ti[6])
        dict["终点站"] = cons.getCityNameWithCode(ti[7])
        dict["出发时间"] = ti[8]
        dict["到达时间"] = ti[9]
        dict["历时"] = ti[10]
        dict["可预订"] = ti[11]  # Y:   N:   IS_TIME_NOT_BUY:
        # dict[""] = ti[12]
        # dict[""] = ti[13]
        # dict[""] = ti[14]
        # dict[""] = ti[15]
        # dict[""] = ti[16]
        # dict[""] = ti[17]
        # dict[""] = ti[18]
        # dict[""] = ti[19]
        # dict[""] = ti[20]
        dict["高等软卧"] = ti[21]
        # dict[""] = ti[22]
        dict["软卧"] = ti[23]
        # dict[""] = ti[24]
        # dict[""] = ti[25]
        dict["无座"] = ti[26]
        # dict[""] = ti[27]
        dict["硬卧"] = ti[28]
        dict["硬座"] = ti[29]
        dict["二等座"] = ti[30]
        dict["一等座"] = ti[31]
        dict["商务座"] = ti[32]
        # dict[""] = ti[33]
        # dict[""] = ti[34]
        # dict[""] = ti[35]
        # dict[""] = ti[36]
        trainDictList.append(dict)

        # c = 0
        # for n in ti:
        #     print('[%s] %s' %(c,n))
        #     c += 1

    cons.saveData(cons.trainDicListPath, trainDictList)
    return trainDictList


# https://www.cnblogs.com/russellwang/p/4174886.html
# https://www.jianshu.com/p/72d0417667e6
# https://www.itsvse.com/thread-4113-1-1.html
# http://blog.csdn.net/javamanjosen/article/details/72676610

# 联系人
# https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs


