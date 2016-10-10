#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#b05505038
#wongchikit


sampleWordList = []                 #1-1
#File=open("C:\Users\user\Desktop\sample.txt","r")
File = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
Text=sampleFile.read()
File.close()
abc = ["?",":","!",".",",","'"]

 for p in abc:
 File=File.replace(p," ")
newfile=File.split(" ")
for a in newfile:                    #a=word
if len(a)>5;
sampleWordList.append(a)
print(sampleWordList)


