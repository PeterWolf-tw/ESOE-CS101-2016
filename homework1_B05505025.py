#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Python 程式的第一、二行一定是如上所示，請不要略過了。

file=open("C:\\Users\\USER\\Desktop\\sample.txt","r")
s=file.read()

q=s.replace("."," ")
w=q.replace("?"," ")
e=w.replace("-"," ")
r=e.replace("1"," ")
t=r.replace("2"," ")
y=t.replace("0"," ")
u=y.replace("\n"," ")
i=u.replace(","," ")

wordlist=i.split(" ")

sampleWordlist=[]

for element in wordlist:
    if len(element) >= 5:
        sampleWordlist.append(element)

print(sampleWordlist)

file.close()



k=0
ending=len(sampleWordlist)

while k < ending :
    if input() in sampleWordlist:
        print("It's in sampleWordlist")
    else:
        print("It's not in the list")







