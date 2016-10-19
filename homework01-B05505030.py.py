sampleFile=open("sample.txt")
sampleText=sampleFile.read()
wordList=sampleText.split(" ")
sampleWordList=[]

for element in wordList:
    if len(element)>5:
      sampleWordList.append(element)
print(sampleWordList)
sampleFile.close()
    
