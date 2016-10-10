#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#HW2 part1 10進位轉2進位

def int2bin(N):    #定義函式
    hankLIST = []    #建立一個空集合
    while N > 0:     #設迴圈
        remainder = int(N % 2)    #取N除以2的餘數
        hankLIST.append(remainder)   #將餘數加進先前設的空集合
        N = (N - remainder) / 2       #N減去餘數在除2，若大於0則再進行下一輪
    ans = ""
    for h in hankLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 h
        ans = ans + str(h)     #將ans加上先前計算之結果以得到最終答案
    return ans   #回傳ans
print(int2bin(N))


#HW2 part2

def ch2(self):
    '''
    請將你計算出來的答案填入以下變數，助教會寫程式自動批改。
    Ch2P2_19a = "xxx"
    意思是
    Ch2   : 第二章
    P2_19a: 第二章結尾處的 PRACTICE SET 段落處的 Problems 第 P2-19 題的 a 小題
    "xxx" ： 你要填入你的答地方。
    '''
    #作業 2. 課本 Ch2. P2.19
    self.Ch2P2_19a = "10"
    self.Ch2P2_19b = "17"
    self.Ch2P2_19c = "6"
    self.Ch2P2_19d = "8"

    #作業 3. 課本 Ch2. P2.20
    self.Ch2P2_20a = "14"
    self.Ch2P2_20b = "8"
    self.Ch2P2_20c = "13"
    self.Ch2P2_20d = "4"

    #作業 4. 課本 Ch2. P2.22
    self.Ch2P2_22a = "00010001 11101010 00100010 00001110"
    self.Ch2P2_22b = "00001110 00111000 11101010 00111000"
    self.Ch2P2_22c = "01101110 00001110 00111000 01001110"
    self.Ch2P2_22d = "00011000 00111000 00001101 00001011"


    def ch3(self):
        '''
        請將你計算出來的答案填入以下變數，助教會寫程式自動批改。
        Ch3P3_28a = "xxx"
        意思是
        Ch3   : 第三章
        P3_28a: 第三章結尾處的 PRACTICE SET 段落處的 Problems 第 P3-28 題的 a 小題
        "xxx" ： 你要填入你的答地方。
        '''
        #作業 5. 課本 Ch3. P3.28
        self.Ch3P3_28a = "234"
        self.Ch3P3_28b = "overflow"
        self.Ch3P3_28c = "874"
        self.Ch3P3_28d = "888"

        #作業 6. 課本 Ch3. P3.30
        self.Ch3P3_30a = "235"
        self.Ch3P3_30b = "overflow"
        self.Ch3P3_30c = "875"
        self.Ch3P3_30d = "889"