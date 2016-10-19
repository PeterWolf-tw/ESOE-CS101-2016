sample=open("./sample.txt","r")
sampleText=sample.read()


k=[".","!","-",'"',"?","0","1","2","\n"]
for e in k:
    sampleText=sampleText.replace(e," ")

wordList=sampleText.split(" ")

sampleWordList=[]
for w in wordList:
    if len(w)>5:
        sampleWordList.append(w)

print(sampleWordList)
sample.close()

counter=1
while counter==1:
    word=input("Please enter a word more than 5 letters  :")
    if len(word) >= 5:
        if word in sampleWordList:
            print(word," is in sampleWordList.")
        else:
            print(word," is not in sampleWordList.")
