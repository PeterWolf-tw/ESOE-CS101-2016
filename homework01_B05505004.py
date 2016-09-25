#1-1
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
        
        





