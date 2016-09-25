a = open("D:/shan/sample.txt","r")
b = a.read()
a.close()

c = b.replace("\n"," ")
d = c.replace('?','')
e = d.replace('"','')
f = e.replace('.','')
g = f.replace(',','')
h = g.replace('-','')

i = h.split(" ")


sampleWordList = [ ]
for j in i:
    if len(j)>5:
        sampleWordList.append(j)
        
print(sampleWordList)


k = input("Guess a word more than five letters: ")
l = 0

while l < 1 :  
    if sampleWordList[0] == k:
        print("You got it!")
        sampleWordList.pop(0)
        l = l + 1
    else:
        print("No!")
        l = l + 1




