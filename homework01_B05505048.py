wilson=open("C:\sample.txt",encoding="utf8")
sampleText=wilson.read()
sampleWordList=[]
k=["0","1","2","3","4","5","6","7","8","9",".",",","(",")","?","!","-",",","\n"]
for m in k:
    sampleText=sampleText.replace(m," ")
        
sampleText_list=sampleText.split(" ")
for v in sampleText_list:
    if len(v)>5:
        sampleWordList.append(v)
print(sampleWordList)
input(sampleWordList)
for x in sampleWordList:
    i=0
    while len(x)>5:
        print("此字在其中")
    else:
        print("此字不在其中")
    
    