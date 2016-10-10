# -*- coding:utf-8 -*-
import collections
file=open('/Users/Raymond/Documents/sample.txt')
context=file.read()
file.close

def charFreqLister(inputSTR):
    LIST=list(inputSTR)
    LIST.remove(punc)
    resultLIST=collections.Counter(LIST)
    return print(resultLIST)
charFreqLister(context)