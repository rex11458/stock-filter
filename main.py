# -*- coding: UTF-8 -*-

# 默认:31949823;佳喜:398410053;沧海:331863675;丰收:260750355;

# 邬佳喜 8686013861817596
# 沧海 8851013789892654
# 丰收 6638013318825774

from filter import filterStocks
from favourite import addStockList, clearStocks, getStockList
from diff import diff
if __name__ == '__main__':
    groups = [
        # {
        #     'userId': '8686013861817596',  # 邬佳喜
        #     'groupId': '398410053'
        # },
        # {
        #     'userId': '8851013789892654',  # 沧海
        #     'groupId': '331863675'
        # },
        {
            'userId': '6638013318825774',  # 丰收
            'groupId': '260750355'
        }
        # ,
        # {
        #     'userId': '5832094130221652',  # 波段
        #     'groupId': '406344906'
        # }
    ]

    # 保存自己的自选股
    selfStocks = getStockList()
    selfStocks.reverse()
    for group in groups:
        print '当前关注的人：%s' % group["userId"]
        stocks = filterStocks(group["groupId"], group["userId"])
        if group["userId"] is '6638013318825774':
            selfStocks = selfStocks + stocks



    # 自己的自选股还原
    clearStocks()
    addStockList(','.join(selfStocks))

    # diff('20200617_8851013789892654.json', '20200618_8851013789892654.json',
    #      '331863675')
    # diff('20200617_8686013861817596.json', '20200618_8686013861817596.json',
    #      '398410053')
    diff('20200618_6638013318825774.json', '20200619_6638013318825774.json',
         '260750355')
