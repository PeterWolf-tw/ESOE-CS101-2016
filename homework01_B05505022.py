#homework1-1
file=open("C:\\Users\mark1\Desktop\sample.txt")
rf=file.read()

mL=['?',',','.','-','\n']

for mark in mL:
    rf2=rf.replace(mark," ")
    
wL=rf2.split(" ")

sampleWordList=[]

for word in wL:
    if len(word) > 5:
        sampleWordList.append(word)
        
print(sampleWordList)

#homework1-2
while True:
    A=input("Please enter a word more than 5 letters :")
    
    if len(A) <= 5:
        print("Please enter a word more than 5 letters\n")
        continue
    if A in sampleWordList:
        print("The word is in sampleWordList\n")
    else:
        print("The word is in sampleWordList\n")