samplefile=open("C:/Users/gj4vu/Desktop/sample.txt",encoding = "utf-8-sig")
text=samplefile.read()
samplefile.close()
mark=["?","-",",",".",'"',"\n","(",")"]
for e in mark:
    text=text.replace(e," ")

text=text.split(" ")
sampleWordList=[]
for h in text:
    if len(text)>5:
        sampleWordList.append(h)
    else:
        pass
    
       
=============================
    
while True:
    a=input("input the word:")
    if len(a)<5:
        print("the word is less than five letter.")
    elif a in sampleWordList:
        print("there is the word")
    else:
        print("nonono")
