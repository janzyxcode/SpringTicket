# _*_ coding: utf-8 _*_

import ngRequest



def checkUser():
    data = {
        "_json_att": ""
    }
    url = 'https://kyfw.12306.cn/otn/login/checkUser'
    return ngRequest.postRequest(url, data)

def submitOrderRequest(trainDate,fromCityName,toCityName,secretStr,dict):
    url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
    data = {
        "train_date": trainDate,
        "back_train_date": trainDate,   #返程，因为是单程票，所以默认选购票日期
        "tour_flag": "dc",                  #票务类型，dc为单程票
        "purpose_codes": "ADULT",
        "query_from_station_name": fromCityName,
        "query_to_station_name": toCityName,
        "undefined": "",
        "secretStr": secretStr
    }
    return ngRequest.postRequest(url,data)


def checkOrderInfo():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
    data = {
        "cancel_flag": 2,
        "bed_level_order_num": "000000000000000000000000000000",
        "passengerTicketStr": "3,0,1,廖乃刚,1,452123198907101937,13622317364,N",       #座位类型,0,票类型(成人/儿童),name,身份类型(身份证/军官证....),身份证,电话号码,保存状态
        "oldPassengerStr": "廖乃刚,1,452123198907101937,1_",
        "tour_flag": "dc",
        "randCode": "",
        "whatsSelect": 1,
        "_json_att": "",
        "REPEAT_SUBMIT_TOKEN": "2be399e93d07d8c6ce218b9a6e57f65e"
    }
    # {"validateMessagesShowId": "_validatorMessage", "status": true, "httpstatus": 200,
    #  "data": {"ifShowPassCode": "N", "canChooseBeds": "N", "canChooseSeats": "N", "choose_Seats": "MOP9",
    #           "isCanChooseMid": "N", "ifShowPassCodeTime": "1", "submitStatus": true, "smokeStr": ""}, "messages": [],
    #  "validateMessages": {}}
    return ngRequest.postRequest(url, data)


def getQueueCount():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
    data = {
        "train_date": "Wed Jan 24 2018 00:00:00 GMT+0800 (CST)",
        "train_no": "6b000K116807",
        "stationTrainCode": "K1168",
        "seatType": 3,
        "fromStationTelecode": "GZQ",
        "toStationTelecode": "CSQ",
        "leftTicket": "gt91IAoZROFZ%2F1XGp24WBbXUD4bG398%2FeGGmfDxoYQHMG5YoULOg0bZSH4Y%3D",
        "purpose_codes": "00",
        "train_location": "Q7",
        "_json_att": "",
        "REPEAT_SUBMIT_TOKEN": "2be399e93d07d8c6ce218b9a6e57f65e"
    }
    # {"validateMessagesShowId": "_validatorMessage", "status": true, "httpstatus": 200,
    #  "data": {"count": "0", "ticket": "306", "op_2": "false", "countT": "0", "op_1": "false"}, "messages": [],
    #  "validateMessages": {}}
    return ngRequest.postRequest(url, data)


def confirmSingleForQueue():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
    data = {
        "passengerTicketStr": "3,0,1,廖乃刚,1,452123198907101937,13622317364,N",
        "oldPassengerStr": "廖乃刚,1,452123198907101937,1_",
        "randCode": "",
        "purpose_codes": "00",
        "key_check_isChange": "F928E24BB8C8E48587A804892CACD72B374EC0AB2722FAF4DDC4ED20",
        "leftTicketStr": "gt91IAoZROFZ%2F1XGp24WBbXUD4bG398%2FeGGmfDxoYQHMG5YoULOg0bZSH4Y%3D",
        "train_location": "Q7",
        "choose_seats": "",
        "seatDetailType": "000",
        "whatsSelect": 1,
        "roomType": "00",
        "dwAll": "N",
        "_json_att": "",
        "REPEAT_SUBMIT_TOKEN": "2be399e93d07d8c6ce218b9a6e57f65e"
    }
    # {"validateMessagesShowId": "_validatorMessage", "status": true, "httpstatus": 200,
    #  "data": {"count": "0", "ticket": "306", "op_2": "false", "countT": "0", "op_1": "false"}, "messages": [],
    #  "validateMessages": {}}
    return ngRequest.postRequest(url, data)


def confirmPassenger():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=1515854548995&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=2be399e93d07d8c6ce218b9a6e57f65e'
    return  ngRequest.getRequest(url)


def resultOrderForDcQueue():
    url = ''
    data = {
        "orderSequence_no": "E865717224",
        "_json_att": "",
        "REPEAT_SUBMIT_TOKEN": "2be399e93d07d8c6ce218b9a6e57f6"
    }