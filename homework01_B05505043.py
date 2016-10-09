#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#samplefile=open("C:/Users/gj4vu/Desktop/sample.txt",encoding = "utf-8-sig")
samplefile = open("./sample.txt", "r", encoding = "utf-8-sig")
#用相對路徑的適用性會更廣一些。
text=samplefile.read()
samplefile.close()
mark=["?","-",",",".",'"',"\n","(",")"]
for e in mark:
    text=text.replace(e," ")

text=text.split(" ")
sampleWordList=[]
for h in text:
    if len(text)>5:
        sampleWordList.append(h)
    else:
        pass


=============================

while True:
    a=input("input the word:")
    if len(a)<5:
        print("the word is less than five letter.")
    elif a in sampleWordList:
        print("there is the word")
    else:
        print("nonono")
