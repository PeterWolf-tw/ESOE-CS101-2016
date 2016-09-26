wilson=open("C:\sample.txt",encoding="utf8")
sampleText=wilson.read()
sampleWordList=[]
k=["0","1","2","3","4","5","6","7","8","9",".",",","(",")","?","!","-",","]
for m in k:
    sampleText=sampleText.replace(m," ")
    
sampleText_list=sampleText.split(" ")
for v in sampleText:
    if len(v)>5:
        sampleWordList.append(v)
print(sampleWordList)
    
    