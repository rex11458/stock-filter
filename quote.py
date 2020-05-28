# -*- coding: UTF-8 -*-

import requests

url = 'http://6.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=100000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f13,f14'


# 获取所有沪深A股
def fetchAllStocks():
    print '获取沪深全量股票...'
    response = requests.get(url)
    stocks = response.json()['data']['diff']

    step = 500

    group = [stocks[i:i + step] for i in range(0, len(stocks), step)]

    return group
