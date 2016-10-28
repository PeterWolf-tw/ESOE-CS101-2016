
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。
#def charFreqLister(inputSTR):
#resultLIST = [(freq, char), (freq, char), (freq, char),...]

#return resultLIST


def charFreqLister(STR):     #定義函式
    
    STR=input("Please enter some words: ")
    length=len(STR)   #計算字串總長度以當分母
    resultLIST=[]     #建立空集合
    
    for n in STR:
        times=STR.count(n)    #計算字串中各字元出現之次數
        fre=times/length      #以fre表示為機率
        resultLIST.append((fre,n))    #將算出知各字元的機率加進先前所建的集合
        
    resultLIST=set(resultLIST)     #將可迭代者建立為set型態的物件
    resultLIST=list(resultLIST)    #將可迭代者建立為list型態的物件
    resultLIST.sort(reverse=True)  #在list內以大到小排列
    
    return(resultLIST)    #回傳




# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for h in inputSTR_X:
        if h == "0":      #在inputSTR_X若為0
            outputSTR = outputSTR + "1"    #則結果為1
        else:    #在inputSTR_X若為1
            outputSTR = outputSTR + "0"   #則結果為0 
    return outputSTR

#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for h in range(0,len(inputSTR_X)) :      
        if inputSTR_X[h]=="1" :    #若inputSTR_X中第h元素為1
            if inputSTR_Y[h]=="1" :   #若inputSTR_Y中第h元素為1
                outputSTR=outputSTR+"1"    #結果為1
            else :                    #若inputSTR_Y中第h元素為0
                outputSTR=outputSTR+"0"    #結果為0
        else:                      #若inputSTR_X中第h元素為0
            outputSTR=outputSTR+"0"       #結果一律為0
      
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    
    for h in range(0,len(inputSTR_X)) :      
        if inputSTR_X[h]=="0" :        #若若中第h元素為0
            if inputSTR_Y[h]=="0" :         #若inputSTR_Y中第h元素為0
                outputSTR=outputSTR+"0"         #結果為0
            else :                          #若inputSTR_Y中第h元素為1
                outputSTR=outputSTR+"1"         #結果為1
        else:                          #若inputSTR_X中第h元素為1
            outputSTR=outputSTR+"1"             #結果一律為1
    
    return outputSTR


#condition00 xor condition04
def condXOR(inputSTR_X, inputSTR_Y):
    
    outputSTR=""
    for h in range(0,len(inputSTR_X)) : 
        if inputSTR_X[h]==inputSTR_Y[h] :    #若inputSTR_X中第h個元素與inputSTR_Y中第h個元素相同
            outputSTR=outputSTR+"0"               #結果為0
        else :                               #若inputSTR_X中第h個元素與inputSTR_Y中第h個元素不同
            outputSTR=outputSTR+"1"               #結果為1
    return outputSTR


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print(condition01)
    
    condition02 = condAND(condition00X,condition00Y)
    print(condition02)
    
    condition03 = condOR(condition00X,condition00Y)
    print(condition03)    
    
    condition04 = condXOR(condition00X,condition00Y)
    print(condition04)    

 # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    print("Ans:")
    Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
    Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
    Ch3P3_20c = "0100 0001 0011 0110 1000 0000 0000 0000"
    Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
    print("========")
    Ch3P3_28a = "765"
    Ch3P3_28b = "439"
    Ch3P3_28c = "-874"
    Ch3P3_28d = "-888"
    print("========")
    Ch3P3_30a = "766"
    Ch3P3_30b = "440"
    Ch3P3_30c = "-875"
    Ch3P3_30d = "-889"
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
