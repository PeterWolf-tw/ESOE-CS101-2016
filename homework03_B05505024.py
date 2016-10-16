# -*- coding:utf-8 -*-

# 作業內容：

# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element
#    已全數完成

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。

file=open('/Users/Raymond/Documents/sample.txt')
context=file.read()
file.close

def charFreqLister(inputSTR):
    LIST=list(inputSTR)
    STRlen=len(inputSTR)
    CHRLIST=[]
    for CHR in LIST:
        if CHR not in CHRLIST:
            CHRLIST.append(CHR)    
    resultLIST=[]
    for CHR in CHRLIST:        
        time=inputSTR.count(CHR)
        freq=time/STRlen
        resultLIST.append((freq,CHR))
        resultLIST.sort(reverse = True)       
    return print(resultLIST)

charFreqLister(context)

# 3.1 加分題：請用課堂中提到的「霍夫曼編碼]
# (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的程式加上轉碼壓縮的功能。

# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition01 not

def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return print(outputSTR)

#condition02 and

def condAND(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):
        if i==j=='1':
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return print(outputSTR)

#condition03 or

def condOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):
        if i==j=='0':
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"        
    return print(outputSTR)

#condition04 xor

def condXOR(inputSTR_X, inputSTR_Y):
    outputSTR = ""
    for i,j in zip(inputSTR_X,inputSTR_Y):    
        if i==j:
            outputSTR = outputSTR + "0"
        else:
            outputSTR = outputSTR + "1"    
    return print(outputSTR)

if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)

print("Ans:")
Ch3P3_20a = "01000000 11100110 00000000 00000000"
Ch3P3_20b = "11000001 01001010 01000000 00000000"
Ch3P3_20c = "01000001 00110110 10000000 00000000"
Ch3P3_20d = "10111110 11000000 00000000 00000000"
print("========")
Ch3P3_28a = "234"
Ch3P3_28b = "560"
Ch3P3_28c = "874"
Ch3P3_28d = "888"
print("========")
Ch3P3_30a = "234"
Ch3P3_30b = "560"
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