#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

"""
Created on Tue Sep 20 22:32:09 2016

@author: steveyeh987
"""

sampleWordList = []
mark_list = ['?',',','-','"','.']

with open("sample.txt",'r') as f:

    for line in f:
        for mark in mark_list:
            line = line.replace(mark,"")
        line = line.strip("\n").split(" ")
        for element in line:
            if len(element) > 5:
                sampleWordList.append(element)

#print "\nsampleWordList: \n"
#print sampleWordList,"\n"
#以上是 Python2 的寫法哦。請改為以下 Python3 的寫法。
print("\nsampleWordList: \n")
print(sampleWordList, "\n")

try:
    found = False
    #x = raw_input("請輸入任何一個五個字母以上的英文字: ")
    #Python2 才有 raw_input()。從 Python3 開始，都是 input()
    x = input("請輸入任何一個五個字母以上的英文字: ")
    assert len(x) > 5
    i = 0
except AssertionError:
   #print "錯誤!輸入英文字少於5個字母!"
   #以上是 Python2 的寫法哦。請改為以下 Python3 的寫法。
    print("錯誤!輸入英文字少於5個字母!")
    #請固定使用四個空格做縮排。


else:
    while(i < len(x)):
        if sampleWordList[i] == x:
            found = True
            break
        i = i + 1

    if found:
        #print "您輸入的字在sampleWordList裡!"
        #以上是 Python2 的寫法哦。請改為以下 Python3 的寫法。
        print("您輸入的字在sampleWordList裡!")
    else:
        #print "您輸入的字不在sampleWordList裡!"
        #以上是 Python2 的寫法哦。請改為以下 Python3 的寫法。
        print("您輸入的字不在sampleWordList裡!")

