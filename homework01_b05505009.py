#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#第一小題
f=open("C:\\Users\\USER\\Desktop\\aaa.txt","r")
x=f.read()

f.close()
a=x.replace("?",'')
b=a.replace('\n',' ')
c=b.replace("2",'')
d=c.replace(',','')
e=d.replace('0','')
f=e.replace('-','')
g=f.replace('.','')
i=g.replace('1','')
j=i.replace('"','')

h=j.split(" ")

samplewordlist=[]

for n in h:
    if len(n)>5:
        samplewordlist.append(n)
        

        
print(samplewordlist)
    
#加分題

while True:
    n=0
    k=0    
    f=input("請輸入一個單字")
    while n < len(samplewordlist):
    
        if samplewordlist[n] == f:
            k = 1
            n = n + 1
        
        else:
            n = n + 1
            
    if k == 1:
        print("the word is in the list") 
    else:
        print("the word is not in the list")
