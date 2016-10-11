#!/usr/bin/env python3
# -*- coding:utf-8 -*-
<<<<<<< HEAD

file = open("C:\.minecraft\Amis.txt","r")
=======
#前兩行請養成習慣宣告程式種類以及編碼

#file = open("C:\.minecraft\Amis.txt","r")
file = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
>>>>>>> f2bfa8fc6fd93b7cab5d018bc2f6ba66c4820e1c
text = file.read()
file.close()

# HW 1-1
text1 = text.replace("\n"," ")
text2 = text1.replace("?"," ")
text = text2.split(" ")
sampleWordList=[]
for h in text:
    if len(h)>=5:
        sampleWordList.append(h)

    else:
        None
print(sampleWordList)


# HW 1-2
a=0


while True:
    key = input("please key in a word more than five letters : ")
    if len(key) < 5:
        print("Not more than five letters \n")
    elif key in sampleWordList:
        print("It is in the sampleWordList.\n")
    else:
        print("Not in sampleWordList.\n")
