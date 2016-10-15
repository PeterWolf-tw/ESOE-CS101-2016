#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#作業1

def numtrans(num):
    num1=str(num)
    l=len(num1)
    n=l-1
    list=[]
    e=0
    while n>-1:
        a=int(num1[n])*pow(2,e)
        list.append(a)
        n=n-1
        e=e+1
    result=sum(list)
    print(num,"的十進位形式是：",result)

#作業2

def digitfinder(prenum):
    eTwo=0
    check=0
    resultlist=[]
    while check<=0:
        check=0
        if pow(2,eTwo)>=prenum:
            check=check+1
            resultlist.append(eTwo)
        else :
            check=check-1
            eTwo=eTwo+1
    print("小於",prenum,"的數字，由二進位表示法最少需要",resultlist[0],"個位元。")


digitfinder(1000)
digitfinder(100000)
digitfinder(64)
digitfinder(256)

#課本 Ch2. P2.19
Ch2P2_19a = "10"
Ch2P2_19b = "17"
Ch2P2_19c = "6"
Ch2P2_19d = "8"
    

#作業3

Ch2P2_20a = "14"
Ch2P2_20b = "8"
Ch2P2_20c = "13"
Ch2P2_20d = "4"

#作業4

P2_22a=[bin(17),bin(234),bin(34),bin(14)]
print(P2_22a)
P2_22b=[bin(14),bin(56),bin(234),bin(56)]
print(P2_22b)
P2_22c=[bin(110),bin(14),bin(56),bin(78)]
print(P2_22c)
P2_22d=[bin(24),bin(56),bin(13),bin(11)]
print(P2_22d)
Ch2P2_22a = "00010001.11101010.00100010.00001110"
Ch2P2_22b = "00001110.00111000.11101010.00111000"
Ch2P2_22c = "01101110.00001110.00111000.01001110"
Ch2P2_22d = "00011000.00111000.00001101.00001011"

#作業5

def ninecom(prenum1):
    res=999-prenum1
    if res>999:
        res=res-1000
    else:
        pass
    print(prenum1,"的nine's complement 是 ",res)

ninecom(234)
ninecom(560)
ninecom(-125)
ninecom(-111)

Ch3P3_28a = "765"
Ch3P3_28b = "439"
Ch3P3_28c = "124"
Ch3P3_28d = "110"

#作業6

def tencom(prenum2):
    resl=1000-prenum2
    if resl>999:
        resl=resl-1000
    else:
        pass
    print(prenum2,"的ten's complement 是 ",resl)
    
tencom(234)
tencom(560)
tencom(-125)
tencom(-111)


Ch3P3_30a = "766"
Ch3P3_30b = "440"
Ch3P3_30c = "125"
Ch3P3_30d = "111"