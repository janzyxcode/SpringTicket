# _*_ coding: utf-8 _*_


import numpy as np
import cv2
import ngRequest
import json
import cons


#https://prateekvjoshi.com/2016/03/01/how-to-read-an-image-from-a-url-in-opencv-python/
def getCaptchaImge():
    print('---2')
    urlStr = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    # response = session.get(urlStr, headers=headers)
    response = ngRequest.getRequest(urlStr)
    print('===0')
    if response.status_code == 200:
        print('===1')
        arr = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)  # 'load it as it is'
        cv2.imwrite(cons.captchaPath,img)
        print('==2')
    return response.status_code




def captchaCheck(positions):
    data = {
        "answer": positions,
        "login_site": "E",
        "rand": "sjrand"
    }
    url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    return ngRequest.postRequest(url,data)

def logout():
    url = 'https://kyfw.12306.cn/otn/login/loginOut'
    return ngRequest.getRequest(url)

def loginReq():
    data = {
        "username": 'liaonaigang',
        "password": "liaonai620",
        "appid": "otn"
    }
    url = 'https://kyfw.12306.cn/passport/web/login'
    return ngRequest.postLoginRequest(url,data)

def uamtk():
    data = {
        "appid": "otn"
    }
    url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
    return ngRequest.postRequest(url,data)

def uamauthclient(newapptk):
    data = {
        "tk": newapptk
    }
    url = 'https://kyfw.12306.cn/otn/uamauthclient'
    return ngRequest.postRequest(url, data)

def initMy12306():
    urlStr = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    return ngRequest.getRequest(urlStr)


# getCaptchaImge()
# print('hello  macos')
