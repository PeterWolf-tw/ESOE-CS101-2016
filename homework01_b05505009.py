#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#f=open("C:\\Users\\user\\Desktop\\sample.txt","r")
f = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
x=f.read()

f.close()
a=x.replace("?",'')
b=a.replace('\n',' ')
c=b.replace("2",'')
d=c.replace(',','')
e=d.replace('0','')
f=e.replace('-','')
g=f.replace('.','')
i=g.replace('1','')
j=i.replace('"','')

h=j.split(" ")

sampleWordList=[]
for k in h:
    if len(k)>5:
        sampleWordList.append(k)

print(sampleWordList)