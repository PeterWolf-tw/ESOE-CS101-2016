#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#1-1
import string
file=open('sample.txt','r')
Text = file.read()

print (Text)
Text = Text.lower() 
file.close()
list=[",","?","0","1","2","-","/","\n" ]
for a in list:
    Text=Text.replace(a," ")
Samplelist=Text.split(" ")
sample_list=[]
count = 0
for b in Samplelist:
    if len(b)>5:
        sample_list.append(b)
        count = count + 1
print(sample_list)        
    
#1-2
time = 0
judge=0
find=input("piease input a word:")
while time<count:
    if find==sample_list[time]:
        print("your word is in sample_list")
        judge=1
        break
    time=time+1
if judge==0:
    print("you had better try it again")
    
