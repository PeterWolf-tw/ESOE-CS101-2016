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

    a=0
    b=0
    ans=0
    myN=N
    while N > 0:
        remainder = int(N % 10)
        a = remainder*(2**b)
        N = (N - remainder) / 10
        b = b+1
        ans=ans+a

    print("{0} 表示為 {1}.".format(myN, ans))
    return None






class HW02:
    def ch2(self):



        #作業 2. 課本 Ch2. P2.19
        self.Ch2P2_19a = "10"
        self.Ch2P2_19b = "17"
        self.Ch2P2_19c = "7"  #"6"
        self.Ch2P2_19d = "9"  #"8"

        #作業 3. 課本 Ch2. P2.20
        self.Ch2P2_20a = "15" #"14"
        self.Ch2P2_20b = "9"  #"8"
        self.Ch2P2_20c = "14" #"13"
        self.Ch2P2_20d = "5"  #"6"

        #作業 4. 課本 Ch2. P2.22
        self.Ch2P2_22a = "00010001 11101010 00100010 00001110"
        self.Ch2P2_22b = "00001110 00111000 11101010 00111000"
        self.Ch2P2_22c = "01101110 00001110 00111000 01001110"
        self.Ch2P2_22d = "00011000 00111000 00001101 00001011"


    def ch3(self):

        #作業 5. 課本 Ch3. P3.28
        self.Ch3P3_28a = "+765"  #"234"
        self.Ch3P3_28b = "+439"  #"560"
        self.Ch3P3_28c = "-874"  #"874"
        self.Ch3P3_28d = "-888"  #"888"

        #作業 6. 課本 Ch3. P3.30
        self.Ch3P3_30a = "+766"  #"234"
        self.Ch3P3_30b = "+440"  #"560"
        self.Ch3P3_30c = "-875"  #"875"
        self.Ch3P3_30d = "-889"  #"889"


if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == 10: #10 是這題的正解。此行檢查這題的答案。
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
        print("Ch2P2_19a:{0}".format("Incorrect!"))
