# -*- coding: UTF-8 -*-

import json
from favourite import addStockList


def diff(file1, file2):
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
    addStockList(','.join(result))


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


diff('20200528_6638013318825774.json', '20200529_6638013318825774.json')
diff('20200528_8686013861817596.json', '20200529_8686013861817596.json')
diff('20200528_8851013789892654.json', '20200529_8851013789892654.json')
