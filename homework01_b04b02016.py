#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
file=open("./sample.txt","r")
story=file.read()
print("The words in sample.txt is:","\n","\n",story,"\n","\n")
story1=story.replace(",","")
story2=story1.replace(".","")
story3=story2.replace("?","")
story4=story3.replace("\n"," ")
list=story4.split(" ")
sampleWordlist=[]
idling=0
for n in range(0,len(list)):
    if len(list[n]) > 5:
        sampleWordlist.append(list[n])
        
    else:
        idling += 1
        
print("The sampleWordlist is ","\n","\n","\t",sampleWordlist,"\n","\n")

n=0
while n==0:
    text=input("請輸入任何一個五個字母以上的英文單字詞：(按空白鍵結束)  ")
    if text==" ":
        n=n+1
    elif len(text) <= 5:
        print(text,"不超過5個字母喔。","\n")
    elif text in sampleWordlist:
        print(text,"在sampleWordlist中。","\n")
    else :
        print(text,"不在sampleWordlist中。","\n")
        