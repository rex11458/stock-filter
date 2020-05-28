# -*- coding: UTF-8 -*-

from quote import fetchAllStocks
from favourite import addStockList, clearStocks, getStockList
from find_stock import saveValidStocks, getValidStocks

globalStocks = fetchAllStocks()

# 保存自己的自选股
selfStocks = getStockList()


def filterStocks(groupId, userId):
    length = len(globalStocks)

    for group in globalStocks:
        # 先清空自选
        length = length-1
        clearStocks()
        stocks = []
        for stock in group:
            item = str(stock['f13']) + '%s%s' % ('.', stock['f12'])
            stocks.append(item)
        addStockList(','.join(stocks))
        saveValidStocks(userId)
        print length

    clearStocks(groupId)
    validStocks = getValidStocks(userId)
    addStockList(','.join(validStocks), groupId)
    print '添加有效自选股成功...'
    # 自己的自选股还原
    clearStocks()
    addStockList(','.join(selfStocks))
