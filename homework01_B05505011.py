#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#1

SampleText=open('/sample.txt',"r")
Text=SampleText.read()
SampleText.close()
SampleWordList=[]
NewText=Text.replace(","," ").replace("."," ").replace("'","").replace("-","").replace("?"," ").replace('"',' ').split()
for n in range(0,len(NewText)):
    if len(NewText[n]) > 5:
        SampleWordList.append(NewText[n])

print(SampleWordList)

#2

while i < i+1 :
    word=str(input("請輸入一個五個字母以上的英文單字\n>>:"))
    if len(word) > 5 :
        if word in SampleWordList:
            print("這個英文單字'有'出現在sampleWordList裡\n")
        else :
            print("抱歉，這個英文單字'沒有'出現在sampleWordList裡\n")
    else:
        print("抱歉，這個英文單字沒有超過五個字母喔\n")