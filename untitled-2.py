#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#您哪位？

sampleFile = open("sample.txt", "r")
rsampleFile = sampleFile.read()
pun=[',','?','0','1','2','-','/','\n','"','.' ]
for a in pun:
    rsampleFile=rsampleFile.replace(a," ")#移除標點符號與換行
wordList = rsampleFile.split(" ")
sampleCounter = 0 # 起始值
sampleWordList = []
while sampleCounter < len(wordList): # 終止條件
    print(wordList[sampleCounter] == wordList[-1])
    if len(wordList[sampleCounter]) > 5:
        sampleWordList.append(wordList[sampleCounter])
        sampleCounter = sampleCounter + 1 # 向「終止條件」靠近一步
    else:
        sampleCounter = sampleCounter + 1

print(sampleWordList)