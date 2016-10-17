#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#===========================================
# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):
    chalist=[]
    freq=[]
    resultLIST=[]
    a=0
    for e in inputSTR:
        if chalist.count(e) == 0:
            chalist.append(e)
            freq = [inputSTR.count(e) / len(inputSTR), str(e)]
            resultLIST.append(freq)
        elif e == " ":
            a+=1
            
        else :
            pass
    b=[a/len(inputSTR)," "]
    resultLIST.append(b)
    sorted(resultLIST, key = lambda resultLIST: resultLIST[0], reverse = True)
    return resultLIST
print (resultList)
#===========================================================
# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    X=inputSTR_X
    Y=inputSTR_Y
    i=0
    output=""
    while i<len(X):       
        if X[i] == Y[i]  and X[i] == "1":
            output+="1"
            i+=1
        else:
            output+="0"
            i+=1
    return output
       

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    X=inputSTR_X
    Y=inputSTR_Y
    i=0
    output=""
    while i<len(X):       
        if  Y[i] == "1" or X[i] == "1":
            output+="1"
            i+=1
        else:
            output+="0"
            i+=1
    return output

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    X=inputSTR_X
    Y=inputSTR_Y
    i=0
    output=""
    while i<len(X):       
        if  Y[i] == X[i]:
            output+="0"
            i+=1
        else:
            output+="1"
            i+=1 
    return output
    

if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    condition02 = condAND(condition00X,condition00Y)
    condition03 = condOR(condition00X,condition00Y)
    condition04 = conXOR(condition00X,condition00Y)

    print(condition01)
    print(condition02)
    print(condition03)
    print(condition04)
#===================================================================================
    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = ""
    Ch3P3_20b = ""
    Ch3P3_20c = ""
    Ch3P3_20d = ""
def IEEE(x):
    x=list(x)
    S=[]
    i=0
    transbefore=[]
    transafter=[]
    if x[0]= "-":
        x=x.pop()
        S.append(1)
    else :
        S.append(0)
    b=bin(int(x))
    b=list(x)
    while True:
        for e in b:
            transbefore.append(e)
            i+=1
            if b[i] == ".":
                break
    E=len(transbefore)-1+127
    E=list(bin(E))
    i=1
    while i<len(x) :
        transafter.append(b[i])
        i+=1
    if i < 23 :
        c=23-i
    M=transafter+[0]*c
    
    ans=S+E+M
    

#==========================================
Ch3P3_28a = "234"
Ch3P3_28b = "560"
Ch3P3_28c = "874"
Ch3P3_28d = "888"

'''
def f(n):
    a=n
    n=str(n)
    if n[0]=="-":
        b=len(n)
        c=10**(b-1)-1+a
        print(c)
    else:
        print(n)
    return None
'''        

#==================================================
Ch3P3_30a = "234"
Ch3P3_30b = "560"
Ch3P3_30c = "875"
Ch3P3_30d = "889"

'''
def f(n):
    a=n
    n=str(n)
    if n[0]=="-":
        b=len(n)
        c=10**(b-1)+a
        print(c)
    else:
        print(n)
    return None
'''   
#=============================================================
print("========")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "00000000"
    Ch4P4_3c = "10011001"
    Ch4P4_3d = "11111111"

def OR(x,y):
    raw=int(x,16)
    a=bin(raw)
    a=list(a)
    a.remove(a[0])
    a.remove(a[0])
    rawy=int(y,16)
    b=bin(rawy)
    b=list(b)
    b.remove(b[0])
    b.remove(b[0])
    print(a,b)
    ans=[]
    i=0
    while  i<len(a):
        if a[i]=="1" or b[i]=="1":
            ans.append("1")
            i+=1
        else :
            ans.append("0")
            i+=1
    ans=''.join(ans)
    print(ans)
========================================
print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "00010001"
    Ch4P4_4d = "10111011"
def AND(x,y):
    raw=int(x,16)
    a=bin(raw)
    a=list(a)
    a.remove(a[0])
    a.remove(a[0])
    rawy=int(y,16)
    b=bin(rawy)
    b=list(b)
    b.remove(b[0])
    b.remove(b[0])
    print(a , b)
    ans=[]
    i=0
    if len(a) < len(b):
        a.insert(0, "0")*(len(b)-len(a))
    if len(a) > len(b):
        b.insert(0, "0")*(len(a)-len(b)) 
    print(a,b)
    while  i<len(a):
        if a[i]==b[i] or b[i]=="1":
            ans.append("1")
            i+=1
        else :
            ans.append("0")
            i+=1
    ans=''.join(ans)
    print(ans)
#============================================
print("========")
    Ch4P4_13a = ""
    Ch4P4_13b = ""
    Ch4P4_13c = ""
    Ch4P4_13d = ""
    
#============================================
print("========")
    Ch4P4_15a = ""
    Ch4P4_15b = ""
    Ch4P4_15c = ""
    Ch4P4_15d = ""
print("========")
    Ch4P4_16a = ""
    Ch4P4_16b = ""
    Ch4P4_16c = ""
    Ch4P4_16d = ""
