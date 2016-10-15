#coding=MS950
file=open("C:\Users\USER\Desktop\sample.txt","r")
noneWordList=["?",".","!",":",";","@","#","$","&","-","2","0"]

A=file.read()

for element in noneWordList:

    B=A.replace(element," ")

    C=B.split(" ")

sampleWordList=[]

for element in C:
    if len(element) > 5:
        sampleWordList.append(element)
        
print(sampleWordList)

file.close()
 