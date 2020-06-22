# -*- coding: UTF-8 -*-

import json
from favourite import addStockList


def diff(file1, file2, groupId="407210032"):
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
    print '-------------------' + groupId + '--------------------------------'
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