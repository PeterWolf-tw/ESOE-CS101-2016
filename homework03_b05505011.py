'''
最最魯的星座?
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
#讀了
# 2. 請試玩 http://armorgames.com/play/17826/logical-element
#玩了
# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST
def charFreqLister(inputSTR):
	charList=[]
	freqList=[]
	resultList=[]
	i=0
	for char in inputSTR:
		if char not in charList:
			charList+=char
'''
建立物件表
'''
	for char in charList:
		freqList+=str(inputSTR.count(char))
'''
各物件出現次數
'''
	for freq in freqList:
		resultList.append((freq,charList[i]))
		i+=1
	resultList.sort(reverse=True)
	return resultList
'''
之後能的話我會盡量簡化
嘗試加入alphabetical order
'''

# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST
# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值
'''
len(inputSTR_X) should be equals to len(inputSTR_Y)
And all the elements in inputSTR_X and inputSTR_Y should be 0 or 1
'''
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
def condAND(inputSTR_X,inputSTR_Y):
	outputSTR=""
	for i in range(0,len(inputSTR_X)):
		if inputSTR_X[i]==inputSTR_Y[i]=="1":
			outputSTR+="1"
		else:
			outputSTR+="0"
	return outputSTR

#condition00 or condition03
def condOR(inputSTR_X,inputSTR_Y):
	outputSTR=""
	for i in range(0,len(inputSTR_X)):
		if inputSTR_X[i]==inputSTR_Y[i]=="0":
			outputSTR+="0"
		else:
			outputSTR+="1"
	return outputSTR
#condition00 xor condition04
> def conXOR(inputSTR_X,inputSTR_Y):
	outputSTR=""
	for i in range(0,len(inputSTR_X)):
		if inputSTR_X[i]==inputSTR_Y[i]:
			outputSTR+="0"
		else:
			outputSTR+="1"
	return outputSTR

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



    

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
'''
Using a bias of 127
'''    
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010010100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111110110000000000000000000000"
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
#all bases are 16
    Ch4P4_3a = "99"
    Ch4P4_3b = "99"
    Ch4P4_3c = "FF"
    Ch4P4_3d = "FF"
    print("========")
#all bases are 16
    Ch4P4_4a = "66"
    Ch4P4_4b = "FF"
    Ch4P4_4c = "11"
    Ch4P4_4d = "BB"
    print("========")
    Ch4P4_13a = "0000010010100000"
    Ch4P4_13b = "1111110010100010"
    Ch4P4_13c = "0000001101011110"
    Ch4P4_13d = "1111101101100000"
    print("========")
#Ans. should be in range -128~127; otherwise they are overflowed or underflowed
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "10110111"
    Ch4P4_15c = "01001001"
    Ch4P4_15d = "underflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "underflow"
'''
Sagittarius
'''
