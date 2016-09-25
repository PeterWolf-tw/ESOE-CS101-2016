a = open("D:/shan/sample.txt","r")
b = a.read()
print(b)

c = b.replace("\n"," ")
x = ['.','?','"']
for n in x:
    d=c.replace(n,"")

e = d.split(" ")


sampleWordList = [ ]
for f in e:
    if len(f)>5:
        sampleWordList.append(f)
        
print(sampleWordList)