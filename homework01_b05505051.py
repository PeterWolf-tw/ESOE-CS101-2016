#homework1-1

sfile=open("sample.txt","r")
stext=sfile.read()
sfile.close()

mark=["0","2","-","?",".","\n",",","\"1"]
swordlist=[]

for element in mark:
    stext=stext.replace(element," ")
    
Stext=stext.split("")

for word in Stext:
    if len(word)>5:
        swordlist.append(word)
    else:
        pass
        
print(swordlist)


#1-2
while true:
    word=input("輸入一個大於五個字的單字")
    if word in swordlist:
        print("這個字在swordlist裡面")
    elif len(word)<=5:
        print("這個單字少於五個字")
    else:
        print("這個字不在swordlist裡面")
