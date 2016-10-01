#Homework Part 1
    #作業 1. 10進位轉2進位
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
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
def ch2(self):
    #作業 2. 課本 Ch2. P2.19
    self.Ch2P2_19a = "10"
    self.Ch2P2_19b = "17"
    self.Ch2P2_19c = "7"
    self.Ch2P2_19d = "9"

    #作業 3. 課本 Ch2. P2.20
    self.Ch2P2_20a = "15"
    self.Ch2P2_20b = "9"
    self.Ch2P2_20c = "14"
    self.Ch2P2_20d = "5"

    #作業 4. 課本 Ch2. P2.22
    self.Ch2P2_22a = "00010001 11111110 00100010 00001110"
    self.Ch2P2_22b = "01101110 00001110 00111000 01001110"
    self.Ch2P2_22c = "00001110 00111000 11111110 00111000"
    self.Ch2P2_22d = "00011000 00111000 00001101 00001011"    
    
def ch3(self):
    #作業 5. 課本 Ch3. P3.28
    self.Ch3P3_28a = "+765"
    self.Ch3P3_28b = "+439"
    self.Ch3P3_28c = "-874"
    self.Ch3P3_28d = "-888"

    #作業 6. 課本 Ch3. P3.30
    self.Ch3P3_30a = "+766"
    self.Ch3P3_30b = "+440"
    self.Ch3P3_30c = "-875"
    self.Ch3P3_30d = "-889"