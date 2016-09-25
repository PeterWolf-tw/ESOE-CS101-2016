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
    A=input("請輸入大於5個字母的詞彙 :")
    
    if len(A) <= 5:
        print("請輸入大於5個字母的詞彙\n")
        continue
    if A in sampleWordList:
        print("此詞彙在sampleWordList內\n")
    else:
        print("此詞彙不在sampleWordList內\n")