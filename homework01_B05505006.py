#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 課後練習1-1
sample = open("./sample.txt", "r")
sample_str = sample.read()
sampleWordList = []
mark = ["0","1","2","3","4","5","6","7","8","9",".",",","-","!","?","\"","\n"]

# 刪掉多餘符號
for c in mark:
    sample_str = sample_str.replace(c, " ")
sample_list = sample_str.split(" ")

# 產生list
for w in sample_list:
    if  len(w) > 5:
        sampleWordList.append(w) 
print(sampleWordList)


# 課後練習1-2
flag = 10

while flag > 0:
    a = input("\n請輸入任何超過五個字母的英文字： ")
    
    if  a.lower() in sampleWordList or a.title() in sampleWordList:
        print( a, "有在 sampleWordList 裡！")
        break
    else:
        if len(a) <= 5:
            print(">>> 你輸入的字沒有超過五個字喔。")
        else:
            print( a, "不在 sampleWordList 裡！")
    
        if flag == 1:
            print(">>> 你沒機會了，掰掰！") 
            flag = -1
        else:
            flag = flag - 1
            print(">>> 你還有 " + str(flag) + " 次機會嘗試。")    

sample.close()
