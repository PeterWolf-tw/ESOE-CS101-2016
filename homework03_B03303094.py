#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。

def charFreqLister(inputSTR):
    lista = []
    resultLIST = []
    for x in inputSTR:
        lista.append(x)
    seta = set(lista)
    for y in seta:
        resultLIST.append('(' + str(lista.count(y) / len(lista)) + ', ' + str(y) + ')')
        resultLIST.sort(reverse = True)
    return resultLIST


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
    outputSTR = ""
    i = 0
    while i < len(inputSTR_X):
        if inputSTR_X[i] != inputSTR_Y[i]:
            outputSTR = outputSTR + "0"
        elif inputSTR_X[i] == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        i = i + 1    
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    i = 0
    while i < len(inputSTR_X):
        if inputSTR_X[i] != inputSTR_Y[i]:
            outputSTR = outputSTR + "1"
        elif inputSTR_X[i] == "0":
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"
        i = i + 1
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    i = 0
    while i < len(inputSTR_X):
        if inputSTR_X[i] != inputSTR_Y[i]:
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
        i = i + 1
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    condition02 = condAND(condition00X, condition00Y)
    print(condition02)
    condition03 = condOR(condition00X, condition00Y)
    print(condition03)    
    condition04 = condXOR(condition00X, condition00Y)
    print(condition04)    


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
    Ch4P4_3a = "0x99"
    Ch4P4_3b = "0x99"
    Ch4P4_3c = "0xFF"
    Ch4P4_3d = "0xFF"
    print("========")
    Ch4P4_4a = "0x66"
    Ch4P4_4b = "0xFF"
    Ch4P4_4c = "0x11"
    Ch4P4_4d = "0xBB"
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