#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

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
    return

def AND(c,d):
    res = ""
    if c == "0":
        res = "0"
    elif c == "1":
        if d == "0":
            res = "0"
        elif d == "1":
            res = "1"
    return res

def compAND(x,y):
    z == ""
    if len(x)!= len(y):
        print('Length are not equals')
        break
    for n in range(0,len(x)):
        neVal = FFFF(x[n],y[n])
        z += newVal
    return z

AND1 = input()
AND2 = input()
ANDANS = compAND(ANDS1,ANDS2)
print(ANDANS)


#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    return

def OR(a,b):
    res = ""
    if a == "1":
        res = "1"
    elif a == "0":
        if b == "0":
            res = "0"
        elif b == "1":
            res = "1"
    return res

def compOR(x,y):
    z == ""
    if len(x)!= len(y):
        print('Length are not equals')
        break
    for n in range(0,len(x)):
        neVal = FFFF(x[n],y[n])
        z += newVal
    return z

OR1 = input()
OR2 = input()
ORANDS = compOR(OR1,OR2)
print(ORANDS)

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    return

def XOR(e,f):
    res = ""
    if e == "0":
        if f == "0":
            res = "0"
        elif f == "1":
            res = "1"
    elif e == "1":
        if f == "0":
            res = "1"
        elif f == "1":
            res = "0"
    return res

def compXOR(x,y):
    z == ""
    if len(x)!= len(y):
        print('Length are not equals')
        break
    for n in range(0,len(x)):
        neVal = FFFF(x[n],y[n])
        z += newVal
    return z
    
XOR1 = input()
XOR2 = input()
XORANS = compXOR(XOR1,XOR2)
print(XORANS)


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "0 1000 0001 110 0110 0000 0000 0000 0000 0000"
    Ch3P3_20b = "1 1000 0010 100 1010 0100 0000 0000 0000 0000"
    Ch3P3_20c = "0 1000 0010 011 0110 1000 0000 0000 0000 0000"
    Ch3P3_20d = "1 0111 1101 100 0000 0000 0000 0000 0000 0000"
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
    Ch4P4_3a = ""
    Ch4P4_3b = ""
    Ch4P4_3c = ""
    Ch4P4_3d = ""
    print("========")
    Ch4P4_4a = ""
    Ch4P4_4b = ""
    Ch4P4_4c = ""
    Ch4P4_4d = ""
    print("========")
    Ch4P4_13a = ""
    Ch4P4_13b = ""
    Ch4P4_13c = ""
    Ch4P4_13d = ""
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
