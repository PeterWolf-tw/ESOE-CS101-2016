#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼
"""
Created on Sun Sep 25 18:31:12 2016
@author: user
"""
"""
===========================================================================
HW1
"""
import string

sampleWordList = []
a = open("./sample.txt","r")
b = a.read()
a.close()

Marks=['?','-','.','"',"\n"]
for e in Marks:
    b=b.replace(e," ")
b=b.replace(',',"")


wordlist=b.split(" ")
for n in wordlist:
    if len(n) >= 5:
        sampleWordList.append(n)
    else:
        pass


print(sampleWordList)
"""
========================================================================
HW2
"""
while True:
	key = input("請打一個英文單字: ")
	if len(key) < 5:
		print("請打一個有5個英文字母以上的英文單字\n")
		continue
	if key in sampleWordList:
		print("這個英文單字在samplewordlist裡面.\n")
	else:
		print("這個英文單字不在samplewordlist裡面.\n")
#請固定使用四個空格做縮排。一個 TAB 鍵和四個空格對程式語言而言有不一樣的意義。


