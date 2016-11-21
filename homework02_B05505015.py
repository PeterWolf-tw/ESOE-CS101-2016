#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#作業 1.
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式供稍後的作業使用：
def bin2int(N):
    tmplist = []
    a=0
    b=0
    while N>0:
        remainder = int(N%10)
        N=(N-remainder)/10
        for t in range(0,b):
           remainder=remainder*2
            #Python 每次縮排是四個空格。上一行只縮了三格！
        b=b+1
        a = a + remainder
        ans=a
        print(ans)







    return None

class HW02:
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
        self.Ch2P2_20d = "4" #"6"

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
        self.Ch3P3_28a = "xxx"
        self.Ch3P3_28b = "xxx"
        self.Ch3P3_28c = "xxx"
        self.Ch3P3_28d = "xxx"

        #作業 6. 課本 Ch3. P3.30
        self.Ch3P3_30a = "xxx"
        self.Ch3P3_30b = "xxx"
        self.Ch3P3_30c = "xxx"
        self.Ch3P3_30d = "xxx"

        #Please finish the assignment ASAP and commit/push again.

if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == 10: #10 是這題的正解。此行檢查這題的答案。
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
        print("Ch2P2_19a:{0}".format("Incorrect!"))