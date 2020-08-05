# -*- coding: UTF-8 -*-

from quote import fetchAllStocks
from favourite import addStockList, clearStocks
from find_stock import saveValidStocks, getValidStocks

globalStocks = fetchAllStocks()


def filterStocks(userId, groupId="31949823"):
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
    return validStocks
