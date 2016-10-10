#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#file =open("D:/sample.txt","r")
file = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
a =file.read()
file.close()

#HW1-1

b =a.replace("\n"," ")
c =b.replace(","," ")
d =c.replace("."," ")
f =d.replace("-"," ")
g =f.replace("?"," ")
h =g.replace("\""," ")
i =h.split(" ")

sampleWordList = [ ]

for j in i:
    if len(j)>=5:
        sampleWordList.append(j)

print(sampleWordList)

#HW1-2

k =0

while k<10000:
    key =input("��J�@�ӶW�L5�Ӧr������r")
    if key in sampleWordList:
        print("�o�ӳ�r���b�峹�̳�!!")
        k =k+1

    elif len(key)<5:
        print("�п�J5�ӳ�r�H�W����r")

    else:
        print("�o��r�S�b�峹��!")
