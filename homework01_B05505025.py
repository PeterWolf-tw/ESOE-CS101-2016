#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#coding=MS950
#file=open("C:\Users\USER\Desktop\sample.txt","r")
file = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
noneWordList=["?",".","!",":",";","@","#","$","&","-","2","0"]

A=file.read()

for element in noneWordList:

    B=A.replace(element," ")

    C=B.split(" ")

sampleWordList=[]

for element in C:
    if len(element) > 5:
        sampleWordList.append(element)

print(sampleWordList)

file.close()
