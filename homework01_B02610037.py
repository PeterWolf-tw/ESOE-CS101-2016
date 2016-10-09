#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#samplefile=open("C:/Users/KUO/Desktop/sample.txt","r",encoding='utf-8')
samplefile = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
sampletext=samplefile.read()
sampleworldlist=[]
other=["0","1","2","3","4","5","6","7","8","9",".",",","?","/","!","-","\n",'"']

for o in other:
    sampletext=sampletext.replace(o," ")
samplelist=sampletext.split(" ")

for w in samplelist:
    if len(w) >5:
        sampleworldlist.append(w)
print(sampleworldlist)


result=False
n=0
x=input("你有10次機會，請輸入任何五個字母以上的英文單字:")
while n < 10:
    if x in sampleworldlist:
        if n < 9:
            print("這個單字有在sampleworldlist裡！歡迎繼續挑戰！")
            resulu=True
            x=input("第"+str(n+2)+"次挑戰，請輸入任何五個字母以上的英文單字:")
            n=n+1
        else:
            print("這個單字有在sampleworldlist裡！")
            print("10次挑戰結束！")
            n=n+1

    else:
        if n < 9:
            print("這個單字沒有在sampleworldlist裡！")
            print("你已經挑戰"+ str(n+1) +"次了！")
            result=False
            x=input("第"+str(n+2)+"次挑戰，請輸入任何五個字母以上的英文單字:")
            n=n+1
        else:
            print("這個單字沒有在sampleworldlist裡！")
            print("10次挑戰結束！")
            n=n+1


samplefile.close()
