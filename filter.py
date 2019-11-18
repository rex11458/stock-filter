# -*- coding: UTF-8 -*-

import requests
from fetch_stocks import getAllStocks
from save_valid_stocks import saveValidStocks, getValidStocks
import time

cookies = {
    "sid":
    "124254159",
    "ct":
    "vo6kbqGcsCsqYI2YRvjz-C7O5ZebiOFrPpZSgWsfpdgXLBYjU4GqODf03-das1arPAUaUUF4lBqb35RBJWzNtcHtfzZZx7PlahbpoN133mP66SzEAbrfbMmrd01Ozk7P_5CsG0ULS6c2HePBVsqeOsAVV1-aQpOWKohir5bbHjo",
    "ut":
    "FobyicMgeV6kJJzUG-FmE-8Kv2NLviJxhRJNNZK_qA_IOk1oF8cAJmdlZXegmv9Bd9JvLfQZVLBBldGbfBhZ_AS2GMNUl7FEv_MUjLWKgoa57gEBwc-Gs4xTDcI2DeeXwmO6QcTVGnz9GoVKS78TaWK9ui6G0go6XIKJJq7zsB5ji8r1FTa7jkcgSOj_yaUqg5MuP3Zy6xDz4oq0mQKDe9UfS0AJ1JjTpqilOZ0ne938oiHF0u0vA5f0kOCTPawRX8-L3SpyB1QgkeheV0KM5X-RedOL5ItE",
    "pi":
    "7273094266403006%3bm7273094266403006%3brexwp%3b7RPJbXuVLTp8lhWg8rANAyqj%2bBJr3MJJVlTACLS7ZnbX8itQvUZAFCb7Guzk6P2tDaIpBh5hoJu8qjuZmHVpwWBmWqFOZMi6NXVGTfeDgjKLtZJ53X7sYTTyo6BVDHaQLKz%2bZH1jpG8%2b941BV5A2ll0Hsj8D9k6sAv3UejDYtbXVAhq0X%2f8Z65y36ObR3P5fjoq624aC%3b9XMqOa%2fhVGr5NYNSInQFpmPzZlP7f%2fN1%2f%2fwnXqBNaPD4rws671LsikBvaX5R6Jtf%2fE4vT4nWOL%2bwOXu7FgZqsvVJJpyKztiF8pZHeMWXk2E3Uh1r020jgzLNNe5k6nt9VeNS4%2biD0tcrt9N3r1iM1usd%2bSTGEg%3d%3d",
    "uidal":
    "7273094266403006rexwp",
    "mobileactivated":
    "1"
}


# 添加自选
def addFavouriteStock(code, market):
    url = "https://myfavor.eastmoney.com/mystock_wap?f=asz&sc=%s|%s|01" % (
        code, market)

    response = requests.get(url, cookies=cookies)
    print response.json().get("data").get("msg")


# 删除自选
def delFavouriteStock(code, market):
    url = "https://myfavor.eastmoney.com/mystock_wap?f=dsz&sc=%s|%s|01" % (
        code, market)

    requests.get(url, cookies=cookies)
    # print code, '|', response.json().get("data").get("msg")


def filterStocks():
    clearFavouriteStocks()
    stocks = getAllStocks()
    index = 0
    while index < len(stocks):
        temp = stocks[index]
        stock = temp.split(",")
        print '---------------', index, '---------------'
        print temp
        code = stock[1]
        market = "0" + stock[0]
        addFavouriteStock(code, market)
        index += 1
        if index % 500 == 0 or index == len(stocks):
            time.sleep(5)
            print 'sleep...'
            saveValidStocks()
            clearFavouriteStocks()

    clearFavouriteStocks()
    print '----------------筛选结束，添加至股票列表-----------------------'
    addValidFavouriteStocks()


def getFavouriteStocks():
    try:
        url = 'https://emwap.eastmoney.com/my/favor/getgroupstocks?id=31949823'
        response = requests.get(url, cookies=cookies)
        return response.json().get('obj')
    except Exception as e:
        print e
        return []


def clearFavouriteStocks():
    print '---------------清除自选列表---------------'
    print '...'
    stocks = getFavouriteStocks()
    for stock in stocks:
        code = stock.get('code')
        mk = stock.get('mk')
        delFavouriteStock(code, mk)
    print '清除完成...'


def addValidFavouriteStocks():
    codes = getValidStocks()
    for code in codes:
        market = "01"
        addFavouriteStock(code, market)
        market = "02"
        addFavouriteStock(code, market)
    print '自选股添加完成...'
