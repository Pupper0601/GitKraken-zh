import hashlib
import json
import time
import uuid
import requests

APP_KEY = "77a5e3bb01dac9d5"
APP_SECRET = "byiap5AqOYZv814BTIpnxcNUDXj3WBcy"


def youdaoTranslate(q):
    """
    note: 将下列变量替换为需要请求的参数
    """
    q = q
    lang_from = 'auto'
    lang_to = 'zh-CHS'
    data = {'q': q, 'from': lang_from, 'to': lang_to}
    addAuthParams(APP_KEY, APP_SECRET, data)

    try:
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = doCall('https://openapi.youdao.com/api', header, data, 'post')
        return json.loads(res.text)["translation"][0]
    except Exception as e:
        print(f"翻译程序错误：{e}")
        return q

def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)


def addAuthParams(appKey, appSecret, params):
    q = params.get('q')
    if q is None:
        q = params.get('img')
    salt = str(uuid.uuid1())
    curtime = str(int(time.time()))
    sign = calculateSign(appKey, appSecret, q, salt, curtime)
    params['appKey'] = appKey
    params['salt'] = salt
    params['curtime'] = curtime
    params['signType'] = 'v3'
    params['sign'] = sign


def calculateSign(appKey, appSecret, q, salt, curtime):
    strSrc = appKey + getInput(q) + salt + curtime + appSecret
    return encrypt(strSrc)


def encrypt(str_src):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(str_src.encode('utf-8'))
    return hash_algorithm.hexdigest()


def getInput(input):
    if input is None:
        return input
    inputLen = len(input)
    return input if inputLen <= 20 else input[0:10] + str(inputLen) + input[inputLen - 10:inputLen]


if __name__ == '__main__':
    createRequest("Sign into a Different Account")
