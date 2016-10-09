#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#Python 利用 # 做為註解標記。你用 < 是無法讓程式執行的。請參考其它同學的寫法。
<<<<<<< HEAD
f=open("./sample.txt","r")
t=f.read()
s2=t.replace("."," ")
s3=s2.replace(","," ")
s4=s3.replace("-"," ")
s5=s4.replace("!"," ")
s6=s5.replace("?"," ")
s7=s6.replace("\n"," ")
t2=s7.split(" ")

sampleWordList = [ ]

for x in t2:
  if len(x) > 5:
    sampleWordList.append(x)
print(sampleWordList)

z=500
while z<1000:
  w= input('please enter a word!')
  if w in  sampleWordList:
    z+=1
    print('exist')
  else:
    z-=1
    print('not exist')






=======
f=open("./sample.txt","r")
t=f.read()
s2=t.replace("."," ")
s3=s2.replace(","," ")
s4=s3.replace("-"," ")
s5=s4.replace("!"," ")
s6=s5.replace("?"," ")
s7=s6.replace("\n"," ")
t2=s7.split(" ")

sampleWordList = [ ]

for x in t2:
  if len(x) > 5:
    sampleWordList.append(x)
print(sampleWordList)

z=500
while z<1000:
  w= input('please enter a word!')
  if w in  sampleWordList:
    z+=1
    print('exist')
  else:
    z-=1
    print('not exist')






>>>>>>> 115fddab22f034af8b8d5acde2e6a3ae5217ed7a
