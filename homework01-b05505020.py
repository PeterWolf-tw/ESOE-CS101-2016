#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

samplefile = open("./sample.txt","r")
sampletext = samplefile.read()


print (str(sampletext) )

samplefile.close()


mark = ["!","?",".",",","'","{","}","[","]","..."]


for n in mark:
    turestory = sampletext.replace(n," ")


print (turestory)






