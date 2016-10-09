#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#s=open("C:/Users/user/Desktop/sample.txt","r")
s = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
sample=s.read()
s.close()
a=['"','(',')','?','!',',','.','\n','[',']','{','}',';',':','-',"'"]
for x in a:
    sample=sample.replace(x,'')
samplelist=sample.split(" ")
samplewordlist=[]
for n in samplelist:
    if len(n)>5:
        samplewordlist.append(n)
    else:
        pass
print(samplewordlist)

while True:
    y=input("enter a word more than five letters:")
    if y in samplewordlist:
        print("in samplewordlist. :)")
    elif len(y)<=5:
        print('you have to enter "more than five" letters!!!')
    else:
        print("sorry, not in samplewordlist.")
