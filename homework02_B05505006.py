#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示。作用等同於 bin(N)
    '''
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print("{0} 的二進位表示為 {1}.".format(N, ans))
    return None


#作業 1.
# 請參考上例，自己寫一個將二進位表示數轉為十進位制的函式供稍後的作業使用：
def bin2int(N):
    '''
    本函式將 bin 二進位制表示數轉為 int 整數
    '''
    N_cal = int(N)
    answer = 0
    for index in range(len(str(N))):
        answer += (N_cal % 10) * (2 ** index)
        N_cal = N_cal // 10
    print("{0} 的十進位表示為 {1}.".format(N, answer))    
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
        self.Ch2P2_19a = "xxx"
        self.Ch2P2_19b = "xxx"
        self.Ch2P2_19c = "xxx"
        self.Ch2P2_19d = "xxx"

        #作業 3. 課本 Ch2. P2.20
        self.Ch2P2_20a = "xxx"
        self.Ch2P2_20b = "xxx"
        self.Ch2P2_20c = "xxx"
        self.Ch2P2_20d = "xxx"

        #作業 4. 課本 Ch2. P2.22
        self.Ch2P2_22a = "xxx"
        self.Ch2P2_22b = "xxx"
        self.Ch2P2_22c = "xxx"
        self.Ch2P2_22d = "xxx"


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


if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == 10: #10 是這題的正解。此行檢查這題的答案。
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
        print("Ch2P2_19a:{0}".format("Incorrect!"))