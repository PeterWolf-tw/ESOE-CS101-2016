sampleFile = open("./sample.txt", "r")
sampleText = sampleFile.read()
sampleFile.close()
sampleText=sampleText.replace("?"," ")
sampleText=sampleText.replace("\n"," ")
sampleText=sampleText.replace("-"," ")
sampleText=sampleText.replace("."," ")
wordList = sampleText.split(" ")
sampleWordList=[]
i=0
for word in wordList:
    if len(word)>5:
        sampleWordList.append(word)
print(sampleWordList)
word2=input("please enter a word with more than five letters")
while i<len(sampleWordList):
        if sampleWordList[i]==word2:
             print("The word is in the samplewordList")
             break
        i=i+1
if  i==len(sampleWordList):
        print("The word is not in the samplewordList") 