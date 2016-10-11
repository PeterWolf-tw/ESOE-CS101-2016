#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#a = open("D:/shan/sample.txt","r")
a = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
b = a.read()
a.close()

c = b.replace("\n"," ")
d = c.replace('?','')
e = d.replace('"','')
f = e.replace('.','')
g = f.replace(',','')
h = g.replace('-','')

i = h.split(" ")
# 從 11 行開始，可以一直用 b 這個變數。程式語言裡遇到「單一一個等號」的時候，先做等號右邊，再把等號右邊的值傳到左邊。
# 因此，b 這個變數可以一直使用下去。反正右邊做完計算的時候，它也不是原來的 b 了，此時我再讓它 b 等於它，意思就是再叫
# 它為「b」。
#e.g.,
#b = b.replace("\n"," ")
#b = b.replace('?','')
#b = b.replace('"','')
#b = b.replace('.','')
#b = b.replace(',','') 
#b = b.replace('-','')
#b = b.split(" ")


sampleWordList = [ ]
for j in i:
    if len(j)>=5:
        sampleWordList.append(j)

print(sampleWordList)


k = input("Guess a word more than five letters: ")
l = 0


while l < 100 :
    if k in sampleWordList:
        print("You got it!")
        l = l + 1
        break
    else:
        print("No!")
        break


