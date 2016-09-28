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
        sampleWordList.append(A)

print(sampleWordList)

while True:
    enter=input("輸入5個字母以上的單字")
    if len(enter)<5:
        print("單字必須大於5個字母!")
        
    elif enter in sampleWordList:
        print(enter,"在sampleWordList裡面!")
        
    else:
        print("不在sampleWordList裡面喔!")

