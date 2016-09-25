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


while True:
    enter=input("請打超過5個字的英文單字:")
    if len(enter)<5:
        print("請打超過5的字母的單字!")
        
    elif enter in sampleWordList:
        print(enter,"在sampleWordList裡面!"
    else:
              print(enter,"不在sampleWordList裡面")
