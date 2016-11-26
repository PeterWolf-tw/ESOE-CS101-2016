#!/usr/bin/env python
# -*- coding: utf-8 -*-
class HW02:
    def ch2(self):
        '''
        請將你計算出來的答案填入以下變數，助教會寫程式自動批改。
        Ch2P2_19a = "xxx"
        意思是
        Ch2   : 第二章
        P2_19a: 第二章結尾處的 PRACTICE SET 段落處的 Problems 第 P2-19 題的 a 小題
        "xxx" ： 你要填入你的答地方。
        #作業 2. 課本 Ch2. P2.19        '''
        self.Ch2P2_19a="010"
        self.Ch2P2_19b="017"
        self.Ch2P2_19c="006"
        #作業 3. 課本 Ch2. P2.20
        self.Ch2P_20a="014"
        self.Ch2P_20b="008"
        self.Ch2P_20c="013"
        self.Ch2P_20d="004"
        #作業 4. 課本 Ch2. P2.22
        self.Ch2P_22a="00010001 11101010 00100010 00001110"
        self.Ch2P_22b="00001110 00111000 11101010 00111000"
        self.Ch2P_22c="01101110 00001110 00111000 01001110"
        self.Ch2P_22d="00011000 00111000 00001101 00001011"
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
        self.Ch3P_28a="234"
        self.Ch3P_28b="560"
        self.Ch3P_28c="874"
        self.Ch3P_28d="888"
        #作業 6. 課本 Ch3. P3.30
        self.Ch3P_30a="234"
        self.Ch3P_30b="560"
        self.Ch3P_30c="875"
        self.Ch3P_30d="889"

        if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
            checkHW02 = HW02()
            checkHW02.ch2()
            if checkHW02.Ch2P2_19a == 10: #10 是這題的正解。此行檢查這題的答案。
                print("Ch2P2_19a:{0}".format("Correct!"))
            else:
                print("Ch2P2_19a:{0}".format("Incorrect!"))
    
    
    
#1
def int2bin(N):
    G=[]
    while N > 0:
        gg=int(N%2)
        G.append(gg)
        N=(N-gg)/2
    G.append(0)
        
    ans=""
    for n in G[::-1]:
        ans=ans+str(n)
    print("{0},{1}".format(N,ans))
    return None
