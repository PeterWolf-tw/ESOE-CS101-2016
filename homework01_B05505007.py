Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #homework01
# -*- coding: utf-8 -*-
#studentID:B05505007
#1-1

import string                                                  #引入模組

spfile = open("./sample.txt","r")
sptext = spfile.read()
spfile.close()
                       
transform = str.maketrans('0123456789\n',"           ",string.punctuation)
sptext    = sptext.translate(transform)
splist    = sptext.split(" ")

sampleWordList = []
for word in splist: 
    if len(word)>5:
    	sampleWordList.append(word)                

print("There are words more than five letters.")
print(sampleWordList)
print("================================================")

#1-2

answer=True
while answer==True:
    userinput=input("input a word more than 5 letters : ")
    if userinput.lower() in sampleWordList or userinput.title() in sampleWordList:
        print(userinput.title(),"is in the article^.^") 
    else:
        if len(userinput)<6:
            print("You idiot,lol.")
        else:
            print(userinput.title(),"is not found.QQ")
        
