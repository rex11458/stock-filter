# -*- coding: UTF-8 -*-

import requests
baseUrl = "http://quote.eastmoney.com/zixuan/api/zxg"

headers = {
    'Content-Type':
    "application/json",
    'Cookie':
    "em_hq_fls=js; pgv_pvi=8388316160; mobileactivated=1; sid=124254159; ct=Z0tCl76fghW_PYoG-HsXoRhfRWVaFdFBVGLZS-LehGgF2dQhII_ILxihuKsKOiAW3ozsi_p32RBDDOY5pJvLeCWZFS6WZYmzzllCgfWbOSASx8vY-_GnAdOldnEDwOSNxPnkSZUr1SMgy5vhhSPwSZ30EvnX1_DwzmXFTx5C2io; ut=FobyicMgeV6kJJzUG-FmE5m_cTsV0z2l3kWb-fF015NMNtf_H_NYZWDjWNMlabZGAVjql4VNjdue8gXV0wDDxRffQf9wydyZ9TO_h69WMlNetIim06tFAXL5teW7Ai_XCbCZ-VWABCX8pqihWbwuZlyfcrO3D-F8iAEpAuTZk1eGQtaP8jKm3_netKdpeWuIucmG910SZwj05GhEryk92LAWuQpqiyiSnArJqog__PVOWV64zgr0SLGskxSoX-M5pwCB6BZ7hjIhwzhAGh1vbA; uidal=7273094266403006rexwp; vtpst=|; intellpositionL=1188px; intellpositionT=490px; HAList=a-sz-002893-%u534E%u901A%u70ED%u529B%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-002815-%u5D07%u8FBE%u6280%u672F%2Ca-sh-603858-%u6B65%u957F%u5236%u836F%2Ca-sz-002881-%u7F8E%u683C%u667A%u80FD%2Ca-sz-002524-%u5149%u6B63%u96C6%u56E2%2Ca-sz-002456-%u6B27%u83F2%u5149%2Cp-sz-832999-%u6CD5%u672C%u4FE1%u606F%2Ca-sz-000820-%u795E%u96FE%u8282%u80FD%2Cf-0-399006-%u521B%u4E1A%u677F%u6307; emshistory=%5B%22510310%22%5D; isoutside=0; st_si=79527022694832; emwap_isEnter=true; st_asi=delete; qgqp_b_id=8cb62c20f565c5c91501b1e7ca727051; st_pvi=34854865705153; st_sp=2019-02-27%2010%3A59%3A40; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=14; st_psi=20200528105954531-113200301712-0425374491",
    'Cache-Control':
    "no-cache",
    'Postman-Token':
    "687f2ee9-455f-4afb-81aa-ee97c30e39c2"
}


# 获取分组信息 [{"id":"31949823","name":"自选股","version":"350435","source":"web"},{"id":"184018443","name":"指数","version":"60","source":"mobile"},{"id":"398410053","name":"佳喜","version":"1","source":"mobile"},{"id":"331863675","name":"沧海","version":"15","source":"mobile"},{"id":"260750355","name":"丰收","version":"22","source":"mobile"},{"id":"354942224","name":"自选","version":"37","source":"web"},{"id":"293024391","name":"板块","version":"32","source":"mobile"},{"id":"366334204","name":"ETF","version":"35","source":"web"},{"id":"74964566","name":"持仓股","version":"1233","source":"web"}]
def getGroupList():
    url = baseUrl + '%s' % "/group"
    # print url
    response = requests.request("GET", url, headers=headers)
    return response.json


# 获取自选股列表
def getStockList(groupId="31949823"):
    url = baseUrl + '%s%s' % ('/getstockbygroupid/', groupId)
    # print url
    response = requests.request("GET", url, headers=headers)
    return response.json()['result']


# 添加单只股票
def addStock(stockcode, groupId="31949823"):
    url = baseUrl + '%s' % ('/addstock')
    payload = {'stockcode': stockcode, 'groupid': groupId}
    response = requests.post(url, json=payload, headers=headers)

    return response.json()


# 批量添加自选股
def addStockList(stocks, groupId="31949823"):
    url = baseUrl + '%s' % ('/movegroup')
    payload = {
        'code': stocks,
        'togroupid': groupId,
        'fromgroupid': '366334204'
    }
    response = requests.post(url, json=payload, headers=headers)
    msg = response.text
    print msg


# 批量删除自选股
def delStockList(stocks, groupId="31949823"):
    url = baseUrl + '%s' % ('/batchdeletestock')
    payload = {
        'codes': stocks,
        'groupid': groupId
    }
    response = requests.post(url, json=payload, headers=headers)
    # msg = response.text
    # print msg


# 自选置顶
def setTop(stock, groupId="74964566"):
    url = baseUrl + '%s' % ('/settop')
    payload = {'code': stock, 'topgroupid': groupId}
    response = requests.post(url, json=payload, headers=headers)
    # print response.text
    return response.json()


# 批量置顶
def setTopList(stocks, groupId="74964566"):
    url = baseUrl + '%s' % ('/movegroup')
    payload = {
        'code': stocks,
        'togroupid': groupId,
        'fromgroupid': '366334204'
    }
    response = requests.post(url, json=payload, headers=headers)
    msg = response.text
    print msg


# 清空自选股
def clearStocks(groupId="31949823"):
    stocks = getStockList(groupId)
    if len(stocks) is 0:
        return
    delStockList(','.join(stocks), groupId)
