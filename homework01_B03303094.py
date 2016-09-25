s=open("C:/Users/user/Desktop/sample.txt","r")
sample=s.read()
s.close()
a=['"','(',')','?','!',',','.','-','\n']
for x in a:
    sample=sample.replace(x,'')
samplelist=sample.split(" ")
samplewordlist=[]
for n in samplelist:
    if len(n)>5:
        samplewordlist.append(n)
    else:
        pass
print(samplewordlist)
