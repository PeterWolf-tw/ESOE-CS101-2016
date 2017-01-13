#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
def charFreqLister(inputSTR):

    resultDict = {}
    resultList = []
    for alpha in inputSTR:
        resultDict[alpha]=0 #將string裡的每個字母放入dictionary並設初始值為0
    for alpha in inputSTR:
        resultDict[alpha]+=1. #計算每個字母出現的次數
    totalAlpha=len(inputSTR)
    for key in resultDict:
        resultDict[key]/=totalAlpha #將次數以機率方式取代
    for key in resultDict:
        resultList.append((resultDict[key],key))  

    for i in range(len(resultList),0,-1):
        for j in range(1,i):
            if (resultList[j][0]>resultList[j-1][0]):   #將resultList對機率進行氣泡排序法
                temp=resultList[j]
                resultList[j]=resultList[j-1]
                resultList[j-1]=temp


    return resultList


# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
def huffmanTranslater(inputSTR):

    resultDict = {}
    resultList = []
    for alpha in inputSTR:
        resultDict[alpha]=0 #將string裡的每個字母放入dictionary並設初始值為0
    for alpha in inputSTR:
        resultDict[alpha]+=1. #計算每個字母出現的次數
    totalAlpha=len(inputSTR)
    for key in resultDict:
        resultDict[key]/=totalAlpha #將次數以機率方式取代
    for key in resultDict:
        resultList.append((resultDict[key],key,0))  

    for i in range(len(resultList),0,-1):
        for j in range(1,i):
            if (resultList[j][0]>resultList[j-1][0]):   #將resultList對機率進行氣泡排序法
                temp=resultList[j]
                resultList[j]=resultList[j-1]
                resultList[j-1]=temp
    i=0
    num=-1
    for item in resultList:
        num+=2**i
        resultList[i]=(resultList[i][0],resultList[i][1],bin(num))    #將huffmanCode加入resultList中
        i+=1
    resultList[len(resultList)-1]=(resultList[len(resultList)-1][0],resultList[len(resultList)-1][1],bin(num//2))


    return resultList


    #return resultList

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
def condAND(inputSTR_X, inputSTR_Y):

    outputSTR = ""
    for i in range(0,len(inputSTR_X)):
        outputSTR += str(int(inputSTR_X[int(i)])&int(inputSTR_Y[int(i)]))

    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    
    outputSTR = ""
    for i in range(0,len(inputSTR_X)):
        outputSTR += str(int(inputSTR_X[int(i)])|int(inputSTR_Y[int(i)]))

    return outputSTR

#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i in range(0,len(inputSTR_X)):
        outputSTR += str(int(inputSTR_X[int(i)])^int(inputSTR_Y[int(i)]))

    return outputSTR

if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    #testcode
    '''STR=input("STR=")
    print(charFreqLister(STR))
    print(huffmanTranslater(STR))
    X=input("X=")
    Y=input("Y=")
    print("condNOT="+condNOT(X))
    print("condAND="+condAND(X,Y))
    print("condOR ="+condOR(X,Y))
    print("condXOR="+condXOR(X,Y))'''

    #testcode

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010010100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111110110000000000000000000000"
    print("========")
    Ch3P3_28a = "765"
    Ch3P3_28b = "439"
    Ch3P3_28c = "874"
    Ch3P3_28d = "888"
    print("========")
    Ch3P3_30a = "766"
    Ch3P3_30b = "440"
    Ch3P3_30c = "875"
    Ch3P3_30d = "889"
    print("========")
    Ch4P4_3a = "0x99"	#"0b10011001"
    Ch4P4_3b = "0x99"	#"0b10011001"
    Ch4P4_3c = "0xFF"	#"0b11111111"
    Ch4P4_3d = "0xFF"	#"0b11111111"
    print("========")
    Ch4P4_4a = "0x66"	#"0b01100110"
    Ch4P4_4b = "0xFF"	#"0b11111111"
    Ch4P4_4c = "0x11"	#"0b00010001"
    Ch4P4_4d = "0xBB"	#"0b10111011"
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
    Ch4P4_16a = "0x1051"
    Ch4P4_16b = "0x102A(overflowed)"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "0x9051(overflowed)"