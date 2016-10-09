#!/usr/bin/env python3        #編碼宣告
# -*- coding:utf-8 -*-



import re

samplefile=open("./sample.txt","r")

sample=samplefile.read()

samplepure=re.findall("[a-zA-Z]+",sample)   #找出英文字

sampleWordList=[]

for s in samplepure:                        #刪除字數<5的英文字
    if len(s)>5:
        sampleWordList.append(s)

print(sampleWordList)

samplefile.close()

#1-2

def judge(a):                                                        #定義一個函數始得輸入錯誤可以重新輸入
    a=input("請輸入一個五個字母以上的英文字:")
    i=0 
    if len(a) > 5:                                                   
        while i< ending:                                             #一個一個嘗試
            for f in sampleWordList:
                if f==a:
                    print("您輸入符合sampleWordList裡的字!")
                    i+=ending
                    break
                else:
                    i+=1
            else:
                print("您未輸入相符的字！")
    else:
        print("您輸入未超過字數底線!") 
        return judge(a)                                               #輸入字母<5可重新輸入
    
    
    
ending=(len(sampleWordList))    

judge("a")