#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼


# Homework1-1




work = open("./sample.txt","r")
watch = work.read()
work.close()

sampleWordList = []


watch = watch.replace("?","")
watch = watch.replace("-","")
watch = watch.replace(".","")
watch = watch.replace(",","")
watch = watch.replace("\n"," ")

result= watch.split(" ")

for n in result:
    if len(n) >= 5:
        sampleWordList.append(n)

print(sampleWordList)

