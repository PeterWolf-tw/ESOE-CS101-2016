#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#f=open(r'C:\Users\user\Desktop\sample.txt')
f = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
sample=f.read()
f.close()

sampletext=sample.replace(',','').replace('"','').replace('.','').replace('?','').replace(' - ','').replace('\n\n',' ')
textlist=sampletext.split(" ")

sampleWordList=[]
for word in textlist:
    if len(word)>5:
        sampleWordList.append(word)
    else:
        Pass
print(sampleWordList)


test=input("Please enter a word more than 5 letters")
while true:
    if len(test)<5:
        print("Read the instruction carefully and try again.")
    elif test in sampleWordList:
        print(test" is in sampleWordList")
    else print(test" is not in sampleWordList")

