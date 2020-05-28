# -*- coding: UTF-8 -*-

import json
import sys
from filter import addFavouriteStock, delFavouriteStock


def diff(file1, file2):
    listA = []
    listB = []
    try:
        with open(file1, 'r') as f:
            listA = json.loads(f.read())
        with open(file2, 'r') as f:
            listB = json.loads(f.read())
    except Exception as e:
        # print e
    result = list(set(listB).difference(set(listA)))

    # print result

    for value in result:
        market = "01"
        delFavouriteStock(value, market)
        addFavouriteStock(value, market)
        market = "02"
        delFavouriteStock(value, market)
        addFavouriteStock(value, market)

    # # 加载cookies
    # coo = requests.cookies.RequestsCookieJar()
    # coo.set('sid', '124254159')
    # coo.set(
    #     'ct',
    #     'vo6kbqGcsCsqYI2YRvjz-C7O5ZebiOFrPpZSgWsfpdgXLBYjU4GqODf03-das1arPAUaUUF4lBqb35RBJWzNtcHtfzZZx7PlahbpoN133mP66SzEAbrfbMmrd01Ozk7P_5CsG0ULS6c2HePBVsqeOsAVV1-aQpOWKohir5bbHjo'
    # )
    # coo.set(
    #     'ut',
    #     'FobyicMgeV6kJJzUG-FmE-8Kv2NLviJxhRJNNZK_qA_IOk1oF8cAJmdlZXegmv9Bd9JvLfQZVLBBldGbfBhZ_AS2GMNUl7FEv_MUjLWKgoa57gEBwc-Gs4xTDcI2DeeXwmO6QcTVGnz9GoVKS78TaWK9ui6G0go6XIKJJq7zsB5ji8r1FTa7jkcgSOj_yaUqg5MuP3Zy6xDz4oq0mQKDe9UfS0AJ1JjTpqilOZ0ne938oiHF0u0vA5f0kOCTPawRX8-L3SpyB1QgkeheV0KM5X-RedOL5ItE'
    # )
    # coo.set(
    #     'pi',
    #     '7273094266403006%3bm7273094266403006%3brexwp%3b7RPJbXuVLTp8lhWg8rANAyqj%2bBJr3MJJVlTACLS7ZnbX8itQvUZAFCb7Guzk6P2tDaIpBh5hoJu8qjuZmHVpwWBmWqFOZMi6NXVGTfeDgjKLtZJ53X7sYTTyo6BVDHaQLKz%2bZH1jpG8%2b941BV5A2ll0Hsj8D9k6sAv3UejDYtbXVAhq0X%2f8Z65y36ObR3P5fjoq624aC%3b9XMqOa%2fhVGr5NYNSInQFpmPzZlP7f%2fN1%2f%2fwnXqBNaPD4rws671LsikBvaX5R6Jtf%2fE4vT4nWOL%2bwOXu7FgZqsvVJJpyKztiF8pZHeMWXk2E3Uh1r020jgzLNNe5k6nt9VeNS4%2biD0tcrt9N3r1iM1usd%2bSTGEg%3d%3d'
    # )
    # coo.set('uidal', '7273094266403006rexwp')
    # coo.set('mobileactivated', '1')
    # sess = requests.session()
    # sess.cookies.update(coo)

    # for value in result:
    #     response = sess.post(
    #         url,
    #         data={
    #             'code': ('0', value),
    #             'topgroupid': '74964566'
    #         })
    #     # print response.text

    #     response = sess.post(
    #         url,
    #         data={
    #             'code': ('1', value),
    #             'topgroupid': '74964566'
    #         })
    #     # print response.text


args = sys.argv

diff(args[1], args[2])
