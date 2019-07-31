# -*- coding: UTF-8 -*-

import requests
import json


# 获取所有沪深A股
def fetchAllStocks():
    url = "https://nufm1.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._A&sty=MPNSBAS&token=4f1862fc3b5e77c150a2b985b12db0fd"
    response = requests.get(url)
    with open('stocks.json', 'w') as f:
        f.write(response.content.replace('(', '').replace(')', ''))


def getAllStocks():
    with open('stocks.json', 'r') as f:
        temp = json.loads(f.read())
    return temp


fetchAllStocks()
