#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#f=open('/users/sample.txt','r')
f = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
F=f.read()
f.close()
a=('?',',','-','"','.','\n','\\')
for x in a:
    F1=F.replace(x,' ')

sampleWordList1=F1.split(' ')

sampleWordList=[]

for y in sampleWordList1:
    if len(y)>5:
        sampleWordList.append(y)

print(sampleWordList)#作業1-1

i=0
while i<3:
    z=input('please type a word with more than 5 letters:')
    if z in sampleWordList:
        i+=1
        print('the word is in the sampleWordList.')
    else:
        print('Bad Luck,try next time.')

        #作業1-2



