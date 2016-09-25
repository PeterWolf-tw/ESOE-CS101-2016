
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
        pass
print(sampleWordList)

#1-2
X=input("Please enter a word over five letters:")
Y=0
while Y<len(sampleWordList):
    if X==sampleWordList[Y]:
        print(X,"is in sampleWordList!")
        break
    elif X!=sampleWordList[Y]:
        Y=Y+1
else:
    print(X,"is not in sampleWordList!")
