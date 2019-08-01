# -*- coding: UTF-8 -*-

import json
import sys


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
    print list(set(listB).difference(set(listA)))


args = sys.argv

diff(args[1], args[2])

diff('2019080109.json', '2019080115.json')
