#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#1-1
samplefile=open("D:/大學/計程/sample.txt",encoding = "utf-8-sig")
#無法使用samplefile = open("./sample.txt", "r", encoding = "utf-8-sig")
text=samplefile.read()
samplefile.close()
mark=["?","-",",",".",'"',"\n","(",")"]
for e in mark:
    text=text.replace(e," ")

b=text.split(" ")
sampleWordList=[]
for h in b:
    if len(h)>5:
        sampleWordList.append(h)
    else:
        pass
print(sampleWordList)
    
       
=============================
1-2    
while True:
    a=input("input the word:")
    if len(a)<5:
        print("the word is less than five letter.")
    elif a in sampleWordList:
        print("there is the word")
    else:
        print("nonono")
