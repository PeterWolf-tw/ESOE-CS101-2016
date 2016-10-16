#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#homework03_b04b02016



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
    outputSTR1=""
    n=0
    while n<int(len(inputSTR_X)):
        if int(inputSTR_X[n])+int(inputSTR_Y[n])==2:
            outputSTR1 = outputSTR1 + "1"
            n=n+1
        else:
            outputSTR1 = outputSTR1 + "0"
            n=n+1
    return outputSTR1

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    outputSTR2=""
    m=0
    while m<int(len(inputSTR_X)):
        if int(inputSTR_X[m])+int(inputSTR_Y[m])==0:
            outputSTR2 = outputSTR2 + "0"
            m=m+1
        else:
            outputSTR2 = outputSTR2 + "1"
            m=m+1
    return outputSTR2

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    outputSTR3=""
    x=0
    while x<int(len(inputSTR_X)):
        if int(inputSTR_X[x])+int(inputSTR_Y[x])==1:
            outputSTR3 = outputSTR3 + "1"
            x=x+1
        else:
            outputSTR3 = outputSTR3 + "0"
            x=x+1    
    return outputSTR3


if __name__== "__main__":
    condition00X = "010111001010100001100011"
    condition00Y = "010000110001011100101001"

    condition01 = condNOT(condition00X)
    print("condition01 is ",condition01)
    
    condition02 = condAND(condition00X,condition00Y)
    print("condition02 is ",condition02)
    
    condition03 = condOR(condition00X,condition00Y)
    print("condition03 is ",condition03)
    
    condition04 = conXOR(condition00X,condition00Y)
    print("condition04 is ",condition04)

#5
print("Ans:")
Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
Ch3P3_20c = "0100 0001 0011 0110 1000 0000 0000 0000"
Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
print("========")
Ch3P3_28a = "765"
Ch3P3_28b = "439"
Ch3P3_28c = "124"
Ch3P3_28d = "110"
print("========")
Ch3P3_30a = "766"
Ch3P3_30b = "440"
Ch3P3_30c = "125"
Ch3P3_30d = "111"
print("========")
str99="10011001"
str00="00000000"
strFF="11111111"
str33="00110011"
a=condOR(str99, str99)
print("4-3a=",a)
Ch4P4_3a = "(99)16"
b=condOR(str99,strFF)
print("4-3b=",b)
Ch4P4_3b = "(FF)16"
c=condOR(str99,str00)
print("4-3c=",c)
Ch4P4_3c = "(99)16"
d=condOR(strFF,strFF)
print("4-3d=",d)
Ch4P4_3d = "(FF)16"
print("========")
e=condNOT(condOR(str99,str99))
print("4-4a=",e)
Ch4P4_4a = "(66)16"
f=condOR(str99,condNOT(str00))
print("4-4b=",f)
Ch4P4_4b = "(FF)16"
g=condOR(condAND(str99,str33),condAND(str00,strFF))
print("4-4c=",g)
Ch4P4_4c = "(11)16"
h=condAND(condOR(str99,str33),condOR(str00,strFF))
print("4-4d=",h)
Ch4P4_4d = "(BB)16"
print("========")
#(a)
print(bin(161))
print(bin(1023))
Ch4P4_13a = "1184"
Ch4P4_13b = "862"
Ch4P4_13c = "-862"
Ch4P4_13d = "-1184"
print("========")
Ch4P4_15a = ""
Ch4P4_15b = ""
Ch4P4_15c = ""
Ch4P4_15d = ""
print("========")
Ch4P4_16a = "0F51"
Ch4P4_16b = "0F2A"
Ch4P4_16c = "8012"
Ch4P4_16d = "7F51"