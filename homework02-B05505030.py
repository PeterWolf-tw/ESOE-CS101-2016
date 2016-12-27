#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Homework Part 1
    #�@�~ 1. 10�i����2�i��
# 程式的第一、二行是固定的。
# 不要把你個人的註解放到第一、二行的位置。

def int2bin(N):
    orgN=N
    Remainders=[]
    while N>0:
        remainder=int(N%2)
        Remainders.append(remainder)
        N=(N-remainder)/2
    Remainders.append(0)

    Ans=""
    for unit in Remainders[::-1]:
        Ans=Ans+str(unit)
    print("{0}(10)={1}(2).".format(orgN,Ans))

if __name__== "__main__":
    int2bin()

#Homework Part 2
# 如果沒有到「類別 (class)」的層級，不會用到 self
def ch2(self):
    #�@�~ 2. �ҥ� Ch2. P2.19
    self.Ch2P2_19a = "10"
    self.Ch2P2_19b = "17"
    self.Ch2P2_19c = "7" #6
    self.Ch2P2_19d = "9" #8

    #�@�~ 3. �ҥ� Ch2. P2.20
    self.Ch2P2_20a = "15" #14
    self.Ch2P2_20b = "9"  #8
    self.Ch2P2_20c = "14" #13
    self.Ch2P2_20d = "5"  #6

    #�@�~ 4. �ҥ� Ch2. P2.22
    self.Ch2P2_22a = "00010001 11111110 00100010 00001110"  #"00010001 11101010 00100010 00001110"
    self.Ch2P2_22b = "01101110 00001110 00111000 01001110"  #"00001110 00111000 11101010 00111000"
    self.Ch2P2_22c = "00001110 00111000 11111110 00111000"
    self.Ch2P2_22d = "00011000 00111000 00001101 00001011"

def ch3(self):
    #�@�~ 5. �ҥ� Ch3. P3.28
    self.Ch3P3_28a = "+765"  #234
    self.Ch3P3_28b = "+439"  #560
    self.Ch3P3_28c = "-874"  #874
    self.Ch3P3_28d = "-888"  #888

    #�@�~ 6. �ҥ� Ch3. P3.30
    self.Ch3P3_30a = "+766"  #234
    self.Ch3P3_30b = "+440"  #560
    self.Ch3P3_30c = "-875"  #875
    self.Ch3P3_30d = "-889"  #889