-homework1-1

sfile=open("sample.txt","r")
stext=sfile.read()

mark=["0","2","-","?",".","\n",",","\"1"]
swordlist=[]

for element in mark:
    stext=stext.replace(element,"")
    
Stext=stext.split("")

for word in Stext:
    if len(word)>5:
        swordlist.append(word)
        
print(swordlist)
sfile.close()


-1-2
