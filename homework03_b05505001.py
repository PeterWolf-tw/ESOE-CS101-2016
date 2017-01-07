#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 3.
word=input("輪入(將表示為['字母',出現機率])：")
lenth=len(word)
wordlist=list(word)
worddictionary={} 
for n in wordlist:
    if n in worddictionary:
        worddictionary[n]=worddictionary[n]+1 
    else:
        worddictionary[n]=1 

wordlist2=list(worddictionary.keys()) 
sequencelist=[]
resultlist=[]
x=0
y=0
for n in wordlist2:
    if worddictionary[n]>0:
        sequencelist.append(((worddictionary[n]/lenth),wordlist2[x])) 
        x=x+1

sequencelist.sort(reverse=True) 

while y<x:
    resultlist.append([sequencelist[y][1],sequencelist[y][0]]) 
    print(resultlist[y])
    y=y+1
    
    
# 4.
#X and Y
def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    cx = 0
    for x in inputSTR_X:
        cy = 0
        for y in inputSTR_Y:
            if cy == cx:
                if x == "1":
                    if y == "1":
                        outputSTR = outputSTR + "1"
                    else:
                        outputSTR = outputSTR + "0"
                else:
                    outputSTR = outputSTR + "0"
            cy = cy+1
        cx = cx+1    
    return outputSTR

#X or Y
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    cx = 0
    for x in inputSTR_X:
        cy = 0
        for y in inputSTR_Y:
            if cy == cx:
                if x == "1":
                    if y == "0":
                        outputSTR = outputSTR + "0"
                    else:
                        outputSTR = outputSTR + "1"
                else:
                    outputSTR = outputSTR + "0"
            cy = cy+1
        cx = cx+1    
    return outputSTR

#X xor Y
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    cx = 0
    for x in inputSTR_X:
        cy = 0
        for y in inputSTR_Y:
            if cy == cx:
                if x == "1":
                    if y == "1":
                        outputSTR = outputSTR + "0"
                    else:
                        outputSTR = outputSTR + "1"
                else:
                    if y == "0":
                        outputSTR = outputSTR + "1"
                    else:
                        outputSTR = outputSTR + "0"
            cy = cy+1
        cx = cx+1    
    return outputSTR
