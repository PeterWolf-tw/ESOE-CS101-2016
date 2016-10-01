# -*- coding: utf-8 -*-
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

print "\nsampleWordList: \n"
print sampleWordList,"\n"

try:
    found = False
    x = raw_input("請輸入任何一個五個字母以上的英文字: ")
    assert len(x) > 5
    i = 0
except AssertionError:
   print "錯誤!輸入英文字少於5個字母!"
else:
    while(i < len(x)):
        if sampleWordList[i] == x:
            found = True
            break
        i = i + 1
        
    if found:
        print "您輸入的字在sampleWordList裡!"
    else:
        print "您輸入的字不在sampleWordList裡!"

