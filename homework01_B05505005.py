
#1-1
S=open("./sample.txt","r")
Stext=S.read()
S.close()
Marks=['?','-','.','"',"\n"]
for e in Marks:
    Stext=Stext.replace(e," ")
Stext=Stext.replace(',',"")

WordList=Stext.split(" ")
sampleWordList=[]
for h in WordList:
    if len(h)>5:
        sampleWordList.append(h)
    else:
        None
print(sampleWordList)