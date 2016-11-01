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

def charFreqLister(inputSTR):
    resultLIST = []
    charDICT = {}
    
    for char in inputSTR:
        if char not in charDICT:
            charDICT[char] = inputSTR.count(char) / len(inputSTR)        
    
    for key in charDICT:
        resultLIST.append((charDICT[key], key))
    
    resultLIST.sort(key=lambda x:x[0], reverse=True)
    return resultLIST


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

import queue

# 令priority queue比較tuple大小時只比較第一項優先值
class TupleSorting(tuple):
    def __lt__(self, other):          #<
        return self[0] < other[0]
    def __gt__(self, other):          #>
        return self[0] > other[0]
    def __le__(self, other):          #<=
        return self[0] <= other[0]
    def __ge__(self, other):          #>=
        return self[0] >= other[0]

def huffmanTranslater(inputSTR):
    resultLIST = []
    freqlist = charFreqLister(inputSTR)
    p = queue.PriorityQueue()
    
    class node:        
        def __init__(self, lc = None, rc = None, char = '', freq = None):
            self.LChild = lc
            self.RChild = rc
            self.char = char
            self.freq = freq
            
        def addCode(self, code = ''):
            if isinstance(self.LChild, node):       # 判斷LChild是否為node
                self.LChild.addCode(code + '0')     # RChild一定同時存在
                self.RChild.addCode(code + '1')     # LChild = None時寫出code
            else:
                resultLIST.append((self.freq, self.char, code))
    
    # 建立終端節點，放入queue（優先值=頻率）
    for x in freqlist:
        newnode = node(None, None, x[1], x[0])
        p.put(TupleSorting((x[0], newnode)))
    
    # 造樹    
    while p.qsize() > 1:
        Left, Right = p.get(), p.get()                      # 取優先值最小的兩個點
        newnode = node(Left[1], Right[1])                   # 創造新節點
        p.put(TupleSorting((Left[0]+Right[0], newnode)))    # 放回queue
    
    (a, root) = p.get()
    root.addCode()
    
    resultLIST.sort(key = lambda x:x[0], reverse=True)
    return resultLIST


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
    for (a, b) in zip(inputSTR_X, inputSTR_Y):
        if a == "1" and b == "1":
            outputSTR += "1"
        else:
            outputSTR += "0"       
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (a, b) in zip(inputSTR_X, inputSTR_Y):
        if a == "0" and b == "0":
            outputSTR += "0"
        else:
            outputSTR += "1"
    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for (a, b) in zip(inputSTR_X, inputSTR_Y):
        if a == b:
            outputSTR += "0"
        else:
            outputSTR += "1"        
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010010100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111110110000000000000000000000"
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
    Ch4P4_15b = "not overflow"
    Ch4P4_15c = "not overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0x0F51"
    Ch4P4_16b = "overflow"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "overflow"
#Good.
