#!/usr/bin/env python3
# -*- coding:utf-8 -*-



#number = 100  #設定 number 這個變數的值為 2
#print("number 的二進位表示法為：{0}".format(bin(number))) 



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

十進位轉二進位(100)
