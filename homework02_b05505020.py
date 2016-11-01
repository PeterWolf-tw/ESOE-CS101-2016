#!/usr/bin/env python3
# -*- coding:utf-8 -*-



x=17


number = int(x)  #設定 number 這個變數的值為 2
print("number 的二進位表示法為：{0}".format(bin(number)))



def 十進位轉二進位(number):
    answer = []
    while number > 0:
        位數 = int(number % 2)
        answer.append(位數)
        number = (number-位數)/2

    answer.append("0b")


    output = ""
    for n in answer[::-1]:
        output = output + str(n)
    print(output)

十進位轉二進位(int(x))



class HW02:
    def ch2(self):
         #作業 2. 課本 Ch2. P2.19
        self.Ch2P2_19a = "10"
        self.Ch2P2_19b = "17"
        self.Ch2P2_19c = "7" #"6"
        self.Ch2P2_19d = "9" #"8"

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
        self.Ch3P3_28a = "234"
        self.Ch3P3_28b = "overflow" #"560"
        self.Ch3P3_28c = "874"
        self.Ch3P3_28d = "888"

        #作業 6. 課本 Ch3. P3.30
        self.Ch3P3_30a = "234"
        self.Ch3P3_30b = "overflow" #"560"
        self.Ch3P3_30c = "875"
        self.Ch3P3_30d = "889"



