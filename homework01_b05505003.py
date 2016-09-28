sampleFile=open("/Users/Tingting/Desktop/sample.txt","r")
sampleText=sampleFile.read()
sampleFile.close()
elements=['.',',','\n','?','-','"','2','000']
for mark in elements:
    sampleText=sampleText.replace(mark," ")
    wordList=sampleText.split(" ")
    cloneList=sampleText.split(" ")
for h in wordList:
    if len(h)<=5:
        cloneList.remove(h)
    else:
        pass
    
print(cloneList)
    















endding=len(story)
for n in range(0,endding-1):
    print(story[n])
    

