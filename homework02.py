#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#<教學>
# 以 "#" 字符號開頭的內容將被 Python 視為「註解」。不會執行。

# #########################################說明########################################
# 對 Python 而言， if __name__ == "__main__" 即為程式的進入點。一個程式只能有「一個」進入點。
# 換言之，整支程式從這一行開始執行。

#def sayHi():
    #'''
    #這裡定義了一個函式，名叫 sayHi
    #'''
    # #這支函式唯一的功能就是印出下面這一句話…
    #print("Hi！這是一支只會說 Hi 的函式。")



#if __name__ == '__main__': #這裡是程式進入點。整支程式從這裡開始執行…
    # #以下執行 sayHi() 函式
    #sayHi()

#</教學>
# #####################################################################################


number = 100  #設定 number 這個變數的值為 2
print("number 的二進位表示法為：{0}".format(bin(number))) #將 2 餵入 bin(n) 函式中，並把 bin(n) 回傳的結果，接著餵給 print() 輸出在螢幕畫面上。

# 你可以試著把 number 的值改為其它的數字，觀察看看。

# bin(n) 的原理大致如下：

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