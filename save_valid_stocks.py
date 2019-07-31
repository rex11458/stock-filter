# -*- coding: UTF-8 -*-
import requests
import json
import re
from datetime import datetime


def getFileName():
    return datetime.now().strftime("%Y%m%d%H") + '.json'


def saveValidStocks():
    url = "http://iguba.eastmoney.com/6638013318825774"
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
    response = requests.get(url, cookies=cookies)
    content = response.content

    try:
        temp = re.findall(r"samestocklist\s=\s\[([^\[\]]*)\];", content)[0]
        stocks = temp.replace('"', '').split(',')
        print '--------------匹配到的股票----------------'
        print stocks
        dumpStocks(stocks)
    except Exception as e:
        print e


def getValidStocks():
    fileName = getFileName()
    try:
        with open(fileName, 'r') as f:
            return json.loads(f.read())
    except Exception as e:
        return []


def dumpStocks(stocks):
    fileName = getFileName()
    old = getValidStocks()
    with open(fileName, 'w') as f:
        try:
            new = list(set(old + stocks))
            json.dump(new, f)
        except Exception as e:
            print e
