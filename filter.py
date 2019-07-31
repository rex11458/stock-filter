# -*- coding: UTF-8 -*-

import requests
from fetch_stocks import getAllStocks
from save_valid_stocks import saveValidStocks, getValidStocks

cookies = {
    "sid":
    "124254159",
    "ct":
    "uO45mgu0M3S6oENVCjMbdQHmu2xdtTSjswmXx5vjkun7QUH_unQ7NRscCu54OI0YJyh1XgY00OjNYHpdzk2o1Sz2RcRw1hfqJK9IrCan1bicASInvh35H3_chF7J2mH5Auwryf7L7bSFE-6dOONDpUYmstGswmVbgZ0zmIjGq-I",
    "ut":
    "FobyicMgeV6kJJzUG-FmE-8Kv2NLviJxhRJNNZK_qA_IOk1oF8cAJmdlZXegmv9Bd9JvLfQZVLD1pyNEC9R0fCxe6wo5M9J3ePwe15fVq9POAYfh4MRvdu40bxJINFr-yPQqTLCIOTC3mzZ8OasCdXJ7oMtrqWazD0lbfURhDqpMXVh_VuEVTldIP4qKpW-KgWaV4d6W3wNe7I4tOMfF03Kw8QgB05Eme7jw8-lbYeKAo11bQXg0LxRj-ARLU4S4TOtUILpip6nqsqfXSYPOQg",
    "pi":
    "7273094266403006%3bm7273094266403006%3brexwp%3b6ke8KvmgSi3IJikLOe%2baVb4HH6nJa9RvP2fw701%2bj3dz42BmW1E23iAG9JMfsZvSM0bxtUNgIY%2bw%2brYirwLVGxIaL%2fUbRmdW%2fpuRhY6LUmhDcGNaYHLkcoUex741D9RhZMHb6%2fHRRxs7ET7%2f6siS3rAGy33CUQiVvfAJmIG%2fTBuxWZxZHDr6sb12UY6l6aY8RZMyKzIi%3b8PqBAMYMvoZH0G83qsqYEybR9BGKphp6A8p3jAi%2byJrdxazE%2by%2f%2fyHSzEr2Jq6iNRiSWcJGxa%2f4uveQMvQ%2bA%2f5JVH82RuKFFmUD8C0iI3e5hrO0GrJz8W8T2s04dJZypxUndw2PtHOnl31Tx%2b4hscsBYyt%2fQRg%3d%3d",
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

    response = requests.get(url, cookies=cookies)
    print code, '|', response.json().get("data").get("msg")


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
        if index % 500 == 0:
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
