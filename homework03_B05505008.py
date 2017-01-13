#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# encoding: utf-8
# B05505008 曾冠維 Python作業三

# 1. 輸入一段字串，並自動計算出字串中，各個字元(包含空白)出現的機率，並由高排到低。

article = input("請輸入任意字串。")
lenth = len(article)
print("字串總字元數為："+ str(lenth) +"\n各字元出現機率由高到低如下：")
word_separate = list(article)
word_dict = {}

for element in word_separate:
    if element in word_dict:
        word_dict[element] = word_dict[element] + 1
    else:
        word_dict[element] = 1
        
char_list = list(word_dict.keys())
seqList = []
resultList = []
i = 0
k = 0

for content in char_list:
    if word_dict[content] > 0:
        seqList.append(((word_dict[content]/lenth),char_list[i]))
        i = i + 1

seqList.sort(reverse = True)

#調整為字元在前，機率在後的表示法

while k < i:
    resultList.append([ seqList[k][1] , seqList[k][0] ])
    print(resultList[k])
    k = k + 1
    
# 5. 課本習題

Ch3P3_20_a = "0 1000 0001 1100 1100 0000 0000 0000 000"
Ch3P3_20_b = "0 1000 0010 0110 1101 0000 0000 0000 000"
Ch3P3_20_c = "1 1000 0010 1001 0100 1000 0000 0000 000"
Ch3P3_20_d = "1 0111 1101 1000 0000 0000 0000 0000 000"

