# -*- coding: UTF-8 -*-

import json
from favourite import addStockList


def diff(file1, file2,groupId):
    listA = []
    listB = []
    try:
        with open(file1, 'r') as f:
            listA = json.loads(f.read())
        with open(file2, 'r') as f:
            listB = json.loads(f.read())
    except Exception as e:
        print e
    result = list(set(listB).difference(set(listA)))
    print result
    addStockList(','.join(result), groupId)


# args = sys.argv

# diff(args[1], args[2])


def intersectionFile(file1, file2, file3):
    try:
        with open(file1, 'r') as f:
            listA = json.loads(f.read())
        with open(file2, 'r') as f:
            listB = json.loads(f.read())
        with open(file3, 'r') as f:
            listC = json.loads(f.read())
    except Exception as e:
        print e
    result = list(set(listB).intersection(set(listA)).intersection(set(listC)))
    print result
    addStockList(','.join(result))

# diff('20200610_6638013318825774.json', '20200617_6638013318825774.json', '260750355')
# diff('20200610_8851013789892654.json', '20200617_8851013789892654.json','331863675')
# diff('20200610_8686013861817596.json', '20200617_8686013861817596.json', '398410053')