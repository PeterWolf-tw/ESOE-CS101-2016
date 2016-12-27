#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):
    resultLIST = []
    import collections
    table = collections.defaultdict(int) # default items will be created using int(), which will return 0
    
    for char in inputSTR:
        table[char] += 1
        
    for key in table:
        resultLIST.append( (table[key], key) ) # (freq, char) = (table[key], key)
        
    from operator import itemgetter
    resultLIST = sorted(resultLIST, key=itemgetter(0), reverse=True) 
    # sorted(...) will return a list which is sorted by first element(at position 0) of the tuple '(freq, char)' in descending order
    
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
    for i in range(0, len(inputSTR_Y)):
        if (inputSTR_X[i] == "1") and (inputSTR_Y[i] == "1"):
            outputSTR += "1"
        else:
            outputSTR += "0"
    return outputSTR


#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in range(0, len(inputSTR_X)):
        if (inputSTR_X[i] == "1") or (inputSTR_Y[i] == "1"):
            outputSTR += "1"
        else:
            outputSTR += "0"
    return outputSTR

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in range(0, len(inputSTR_X)):
        if inputSTR_X[i] == "1":
            outputSTR += condNOT(inputSTR_Y[i])
        else:
            outputSTR += inputSTR_Y[i]
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    '''
    str = input("input:")
    print(charFreqLister(str))
    '''
    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    # finished at 2016/12/11 
    print("Ans:")
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010010100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111111101100000000000000000000"
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
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "no overflow"
    Ch4P4_15c = "no overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0x0F51"
    Ch4P4_16b = "0x0F2A"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "overflow"