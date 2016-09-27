#1-1
#coding=utf-8

import re

samplefile=open("./sample.txt","r")

sample=samplefile.read()

sample=re.sub("\d"," ",sample)
sample=re.sub("\s"," ",sample)
deletion = [".",",","-","!","?","\"","\n"]

for d in deletion:
    sample = sample.replace(d, " ")

sample=sample.split()

sampleWordList=[]

for s in sample:
    if len(s)>5:
        sampleWordList.append(s)

print(sampleWordList)

samplefile.close()

#1-2

test=input("請輸入任意五個字母以上的單字：")


ending=(len(sampleWordList))
i=0

if len(test) > 5:
        while i< ending:
            for f in sampleWordList:
                if f==test:
                    print("您輸入符合sampleWordList裡的字!")
                    i+=ending
                    break
                else:
                    i+=1
            else:
                print("您未輸入相符的字！")
else:
    print("您輸入未超過字數底線!")
    
