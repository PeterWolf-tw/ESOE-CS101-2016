file=open("sample.txt","r")
text=file.read()
file.close()
sampleWordList=[]
x=["?","\n",",","-",'"',"."]
for element in x:
    text=text.replace(element," ")
wordList=text.split(" ")
for element in wordList:
    if len(element)>5:
        sampleWordList.append(element)
    else:
        pass
print(sampleWordList)

Q=input("Enter a word that is longer than five letters:")
count=0
while count<len(sampleWordList):
    if Q in sampleWordList:
        print("It's in the sampleWordList.")
        break
    else:
        print("It's NOT in the sampleWordList.")
        break
