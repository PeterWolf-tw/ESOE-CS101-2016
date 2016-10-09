#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

sampleFile=open("sample.txt")
sampleText=sampleFile.read()
wordList=sampleText.split(" ")
sampleWordList=[]

for element in wordList:
    if len(element)>5:
      sampleWordList.append(element)
    #請固定使用四個空格做縮排。
print(sampleWordList)
sampleFile.close()

