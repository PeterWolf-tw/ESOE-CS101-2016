
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST


def charFreqLister(STR):     #定義函式
    
    STR=input("Please enter some words: ")
    length=len(STR)   #計算字串總長度以當分母
    resultLIST=[]     #建立空集合
    
    for n in STR:
        times=STR.count(n)    #計算字串中各字元出現之次數
        fre=times/length      #以fre表示為機率
        resultLIST.append((fre,n))    #將算出知各字元的機率加進先前所建的集合
        
    resultLIST=set(resultLIST)     #將可迭代者建立為set型態的物件
    resultLIST=list(resultLIST)    #將可迭代者建立為list型態的物件
    resultLIST.sort(reverse=True)  #在list內以小到大排列
    
    return(resultLIST)    #回傳


print(charFreqLister(""))