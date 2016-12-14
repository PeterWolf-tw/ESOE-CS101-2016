#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼

#read the file from the sample.txt
wordfile=open("./sample.txt","r", encoding="utf8")
wordtext=wordfile.read()
#killing the marks
wordtext1=wordtext.replace("\n"," ")
wordtext2=wordtext1.replace("?"," ")
wordtext3=wordtext2.replace('"'," ")
wordtext3=wordtext3.replace("?"," ")
wordtext3=wordtext3.replace("\""," ")
wordtext3=wordtext3.replace("."," ")
wordtext3=wordtext3.replace(",","")
#define an empty list
sampleWordList=[""]
#change the string into a list
sampleWord=wordtext3.split()
#HW1-1
for sampleWordList1 in sampleWord:
#OK miss the "="!!!!!!
    if len(sampleWordList1)>=5:
#add the five or above letter words into the list
        sampleWordList.append(sampleWordList1)
        print(sampleWordList1)
#HW1-2
#loop starting
whilecount=1
while whilecount:
#user type in the word
    ans=input("please enter your answer= ")
#if the the word is lesser than five LETTERS
    if len(ans)<5:
        print("Please enter more that 5 letters")
        whilecount=whilecount+1
#if the user got it
    elif ans in sampleWordList:
        print( "you keyed in "+ans)
        whilecount=whilecount+1
#if the word isnt on the list
    else:
        print("sorry not found, try again")
        whilecount=whilecount+1
#change log
         # added the "kill mark" code
         #I can use this!
         #I consider 2000th as a letter this change is to clairfy that.
         #2016/10/9   fixed the problem that you can't find the a word that is equal to five letters.