#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#FiL= open("C:\User\BiaHD\sample.txt","r")                                             #作業1-1部分
FiL = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
FiT= FiL.read()
FiL.close()
sampleWordList = []

move = ["!","-",":","'",";","?",",",".","．．．","<",">","[","]","(",")","/","{","}"]

for pun in move:
    FiT=FiT.replace(pun," ")
    Flist=FiT.split(" ")
for word in Flist:
    if len(word) > 5;
       sampleWordList.append(word)
#請固定使用四個空格做縮排。
print ("Get sampleWordList! ")
print (sampleWordList)                                                                #作業1-1部分結束
print (''' ''')



end = False                                                                           #作業1-2部分
N = 0
Your importation = input("請隨意輸入任何-超過-五個英文字母以上的單字")
# 變數名稱不能留空格！
while N < len(sampleWordList):
    if sampleWordList[N] == Your importation:
        end == True
        N=N+1
        print(''' ''')
    if end == True:
        print("恭喜你輸入的單字剛好在sampleWordList裡")
        print(''' ''')
    else:
        print("很可惜，它並不在sampleWordList裡")                                       #作業1-2部分結束
        print(''' ''')















