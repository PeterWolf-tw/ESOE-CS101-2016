#Part1-1
import string                                 

spfile=open("./sample.txt","r")
sptext=spfile.read()
spfile.close()
                       
intab='0123456789][]}{\n?".!,:;()'           #delete numbers and all kinds of punctuations
outtab='                         '           #空格要和intab元素一樣多(一一對應)         
trantab=str.maketrans(intab,outtab)        
sptext=sptext.translate(trantab)


splist=sptext.split(" ")


sampleWordList=[]
for word in splist: 
    if len(word)>5:
    	sampleWordList.insert(-1,word)

print(sampleWordList)

#Part1-2 



