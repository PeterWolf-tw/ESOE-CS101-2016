#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。

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

# 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
print("Ans:")
Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
Ch3P3_20c = "0100 0001 0011 0110 1000 0000 0000 0000"
Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
print("========")
Ch3P3_28a = "234"
Ch3P3_28b = "overflow"
Ch3P3_28c = "874"
Ch3P3_28d = "888"
print("========")
Ch3P3_30a = "234"
Ch3P3_30b = "overflow"
Ch3P3_30c = "875"
Ch3P3_30d = "889"
print("========")
Ch4P4_3a ="11011101"