# -*- coding: UTF-8 -*-
import requests
import json

from datetime import datetime


def getFileName():
    return datetime.now().strftime("%Y%m%d%H") + '.json'


def saveValidStocks():
    url = "http://i.eastmoney.com/api/getsamestock?f=gcomstks&top=500&u=6638013318825774&_=1571035178980"
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
    response = requests.get(url, cookies=cookies)
    content = response.json()
    stocks = []
    try:
        result = content["result"].split(',')
        for value in result:
            stocks.append(value[2:])
            pass
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
