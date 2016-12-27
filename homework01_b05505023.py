#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#2==========HW1-1
f=open("./sample.txt","r")
t=f.read()
s2=t.replace("."," ")
s3=s2.replace(","," ")
s4=s3.replace("-"," ")
s5=s4.replace("!"," ")
s6=s5.replace("?"," ")
s7=s6.replace("\n"," ")
t2=s7.split(" ")



#=======================================homework1-2


while True :
  z = input('please enter a word!')
  if z in sampleWordList:
    print('exist')
    continue
  else:
    print('not exist')

    continue
t=f.close()
   





