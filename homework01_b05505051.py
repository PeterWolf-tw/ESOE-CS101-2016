#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

-homework1-1
#Python 以 # 號為註解符號。而非 - 號。

sfile=open("sample.txt","r")
stext=sfile.read()

mark=["0","2","-","?",".","\n",",","\"1"]
swordlist=[]

for element in mark:
    stext=stext.replace(element,"")

Stext=stext.split("")

for word in Stext:
    if len(word)>5:
        swordlist.append(word)

print(swordlist)
sfile.close()


-1-2
while true:
    word=input("��J�@�Ӥj�󤭭Ӧr����r")
    if word in swordlist:
        print("�o�Ӧr�bswordlist�̭�")
    elif len(word)<=5:
        print("�o�ӳ�r�֩󤭭Ӧr")
    else:
        print("�o�Ӧr���bswordlist�̭�")
