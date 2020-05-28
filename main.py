# -*- coding: UTF-8 -*-

# 默认:31949823;佳喜:398410053;沧海:331863675;丰收:260750355;

# 邬佳喜 8686013861817596
# 沧海 8851013789892654
# 丰收 6638013318825774

from filter import filterStocks

if __name__ == '__main__':
    groups = [
        {
            'userId': '8686013861817596',  # 邬佳喜
            'groupId': '398410053'
        },
        {
            'userId': '8851013789892654',  # 沧海
            'groupId': '331863675'
        },
        {
            'userId': '6638013318825774',  # 丰收
            'groupId': '260750355'
        },
    ]

    for group in groups:
        print '当前关注的人：%s' % group["userId"] 
        filterStocks(group["groupId"], group["userId"])