#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#homework1-1

sfile=open("sample.txt","r")
stext=sfile.read()

mark=["0","2","-","?",".","\n",",","\"1"]
swordlist=[]

for element in mark:
    stext=stext.replace(element,"")
    
Stext=stext.split(" ")

for word in Stext:
    if len(word)>5:
        swordlist.append(word)
        
print(swordlist)
sfile.close()


#1-2
word=input("輸入一個大於五個字的單字")
while true:
    if word in swordlist:
        print("這個字在swordlist裡面")
    elif len(word)<=5:
        print("這個單字少於五個字")
    else:
        print("這個字不在swordlist裡面")
