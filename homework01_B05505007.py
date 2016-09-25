#1-1
# -*- coding: utf-8 -*-
#studentID:B05505007
import string                                                  #引入模組

spfile = open("./sample.txt","r")
sptext = spfile.read()
spfile.close()
                       
transform= str.maketrans(string.digits,"          ",string.punctuation)
sptext= sptext.translate(transform)

splist = sptext.split(" ")

sampleWordList = []

for word in splist: 
    if len(word)>5:
    	sampleWordList.insert(-1,word)                         #note:.insert(-1,word)==.append(word)

print("There are words more tha five letters.")
print(sampleWordList)
print("===============================")

#1-2

answer=True
while answer==True:
    userinput=input("input a word more than 5 letters : ")
    if userinput.lower() in sampleWordList or userinput.title() in sampleWordList:
        print("it is in the article^.^") 
    else:
        if len(userinput)<6:
            print("You idiot lol")
        else:
            print("Sorry it is not found.QQ")
        
 


        
        	

    


