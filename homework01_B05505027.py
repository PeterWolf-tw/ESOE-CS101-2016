#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#Homework1-1-------------------------------------------------------


#讀取檔案並轉為可讀文字
f1=open("sample.txt","r")
f2=f1.read()
f1.close()

#刪除非必要符號並分割詞彙
f3=f2.replace("-"," ")
f3=f3.replace("."," ")
f3=f3.replace("?"," ")
f3=f3.replace(","," ")
f3=f3.replace("0"," ")
f3=f3.replace("1"," ")
f3=f3.replace("2"," ")
f3=f3.replace("\""," ")
f3=f3.replace("\n"," ")
f4=f3.split(" ")

#生成列表並篩選列表詞彙
sampleWordList=[]

end=len(f4)
n=0
while n<=end-1:
	if len(f4[n])>5:
		sampleWordList.append(f4[n])
		n+=1
	else:
		n+=1
#請固定使用四個空格做縮排。一個 TAB 鍵和四個空格對程式語言而言有不一樣的意義。

#產出列表
print(sampleWordList)
print("\n")

#Homework1-2-------------------------------------------------------
#請固定使用四個空格做縮排。一個 TAB 鍵和四個空格對程式語言而言有不一樣的意義。

x=0
while x<1:
    word=input("please type a word with more than 5 letters.\n")#輸入詞彙
    if len(word)<5:#判定詞彙是否超過五個字
                print("the word is not long enough!")
    else:
                if word in  sampleWordList:#判定詞彙是否存在列表裡
                    print("this word exist in the list!"+"\ntry again?")
                else:
                    print("this word doesn't exist in the list!"+"\ntry again?")



