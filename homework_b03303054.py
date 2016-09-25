f=open("D:/sample.txt","r")
t=f.read()
f.close()

sampleWordList=[]
marklist = [".","!","?",",","—","\"","\n","\'"]
for mark in marklist:
    t=t.replace(mark," ")

t=t.split(" ")
for A in t:
    if len(A)>5:
        sampleWorkList.append(A)

print(sampleWordList)



