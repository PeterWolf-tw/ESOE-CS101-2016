#!/usr/bin/env python3
    +# -*- coding:utf-8 -*-
    +
    +
    +# 繳交日期：2016.10.17
    +
    +# 作業內容：
    +# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)
    +
    +# 2. 請試玩 http://armorgames.com/play/17826/logical-element
    +
    +# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
    +#    並由高排到低。
    
    +#def charFreqLister(inputSTR):
    +#resultLIST = [(freq, char), (freq, char), (freq, char),...]
    +
    +#return resultLIST
    def charFreqLister(inputSTR):
        
        character=input("請輸入文字")
        print("輸入文字為:",character)
        
         characterLen=len(character)#計算文字長度
       
        resultLIST=[]
        
        for x in character:
            arise=character.count(x)#文字出現次數
            frequency=arise/characterLen#機率
            resultLIST.extend((frequency,x))#把這個放入
            s=set(resultLIST)
            resultLIST=list(s)
            resultLIST.sort(resyltLIST,key=itemgetter(0), reverse= True)
            return resultLIST
    +# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
    +#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
    +#     程式加上轉碼壓縮的功能。
    +# e.g.,
    +#def huffmanTranslater(inputSTR):
    +#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]
    +
    +#return resultLIST
    +
    +# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值
    +
    +#condition00 not condition01
    +def condNOT(inputSTR_X):
    +    outputSTR = ""
    +    for i in inputSTR_X:
    +        if i == "0":
    +            outputSTR = outputSTR + "1"
    +        else:
    +            outputSTR = outputSTR + "0"
    +    return outputSTR
    +
    +
    +#condition00 and condition02
    +def condAND(inputSTR_X, inputSTR_Y):
    +outputSTR =" "
     for(x,y)in zip(inputSTR_X, inputSTR_Y):
     if x=="1"and y=="1":
     outputSTR+="1"
     else:
          outputSTR+="0"
   return outputSTR 
    return
    +
    +#condition00 or condition03
    +def condOR(inputSTR_X, inputSTR_Y):
    +  outputSTR =" "
       for(x,y)in zip(inputSTR_X, inputSTR_Y):
       if x=="0" or y=="0":
        outputSTR+="0"
        else:
            outputSTR+="1"   
    return
    +
    +#condition00 xor condition04
    +def conXOR(inputSTR_X, inputSTR_Y):
    + outputSTR=" "
      for(x,y)in zip(inputSTR_X, inputSTR_Y):
      if x==y:
            outputSTR+="0"
        else:
            outputSTR+="1"   
    return
    +
    +
    +if __name__== "__main__":
    +    condition00X = "010111001010100001100011"
    +    condition00Y = "010000110001011100101001"
    +
    +    condition01 = condNOT(condition00X)
    +    print(condition01)
    +
    +    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    +    print("Ans:")
    +    Ch3P3_20a = "01000000111001100000000000000000"
    +    Ch3P3_20b = "11000000110101001000000000000000"
    +    Ch3P3_20c = "01000001001101101000000000000000"
    +    Ch3P3_20d = "10111110110000000000000000000000"
    +    print("========")
    +    Ch3P3_28a = "234"
    +    Ch3P3_28b = "overfiow"
    +    Ch3P3_28c = "874"
    +    Ch3P3_28d = "888"
    +    print("========")
    +    Ch3P3_30a = "234"
    +    Ch3P3_30b = "560"
    +    Ch3P3_30c = "875"
    +    Ch3P3_30d = "888"
    +    print("========")
    +    Ch4P4_3a = "99"
    +    Ch4P4_3b = "99"
    +    Ch4P4_3c = "FF"
    +    Ch4P4_3d = "FF"
    +    print("========")
    +    Ch4P4_4a = "66"
    +    Ch4P4_4b = "FF"
    +    Ch4P4_4c = "11"
    +    Ch4P4_4d = "BB"
    +    print("========")
    +    Ch4P4_13a = "1184"
    +    Ch4P4_13b = "-862"
    +    Ch4P4_13c = "862"
    +    Ch4P4_13d = "-1184"
    +    print("========")
    +    Ch4P4_15a = "overflow"
    +    Ch4P4_15b = "overflow"
    +    Ch4P4_15c = "no overflow"
    +    Ch4P4_15d = "overflow"
    +    print("========")
    +    Ch4P4_16a = "0x1051"
    +    Ch4P4_16b = "overflow"
    +    Ch4P4_16c = "0x8012"
    +    Ch4P4_16d = "overflow"