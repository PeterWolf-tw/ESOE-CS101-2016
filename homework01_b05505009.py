f=open("C:\\Users\\user\\Desktop\\sample.txt","r")
x=f.read()

f.close()
a=x.replace("?",'')
b=a.replace('\n',' ')
c=b.replace("2",'')
d=c.replace(',','')
e=d.replace('0','')
f=e.replace('-','')
g=f.replace('.','')
i=g.replace('1','')
j=i.replace('"','')

h=j.split(" ")

sampleWordList=[]
for k in h:
    if len(k)>5:
        sampleWordList.append(k)

print(sampleWordList)