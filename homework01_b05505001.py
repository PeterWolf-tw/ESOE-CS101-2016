#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#part1.1
file = open("sample.txt", encoding='utf-8-sig')
replace = file.read().replace("\n"," ").replace("?","").replace(".","").replace("-","")
file.close()
sample = replace.split(" ")
sampleWordList = []
for n in range(0,len(sample)):
    if len(sample[n]) > 5 :
        sampleWordList.append(sample[n])

print(sampleWordList)
#part1.2
asking = 1

while asking > 0:
    #test = input()
    #加個提示吧，否則使用者不知道發生了什麼事。
    test = input("請輸入一個英文字：")
    if test in sampleWordList:
        print(test + " is in sampleWordList")
    else:
        print(test + " is not in sampleWordList")

