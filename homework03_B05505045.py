#!/usr/bin/env python
# -*- coding: utf-8 -*-
def charfreq(inputstr):
    resultlist=[]
    freq=[]
    for n in inputstr:
        freq=inputstr.count(n)/len(inputstr)
        resultlist.append((freq,n))
    resultlist.sort(reverse=True)
    print(resultlist)
    
    return resultlist

            
                
         
# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR=""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR    

#condition00 and condition02
def condAND(inputstrx, inputstry):
    
    outputstr=""
    for (a,b) in (inputstrx,inputstry):
        if a == b =="1":
            outputstr+="1"
        else:
            outputstr+="0"
        
            return outputSTR    
#condition00 or condition03
def condOR(inputstrx,inputstry):
    
    outputstr=""
    for (a,b) in (inputstrx,inputstry):
        if a|b == "1":
            outputstr+="1"
        else:
            outputstr+="0"
           
            return outputSTR 
#condition00 xor condition04
def condXOR(inputstrx,outputstry):
    
    outputstr=""
    for (a,b) in (inputstrx,inputstry):
        if a == b :
            outputstr+="0"
        else:
            outputstr+="1"

            return outputSTR
            
        
            
            