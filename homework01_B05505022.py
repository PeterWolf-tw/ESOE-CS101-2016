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
    A=input("�п�J�j��5�Ӧr�������J :")
    
    if len(A) <= 5:
        print("�п�J�j��5�Ӧr�������J\n")
        continue
    if A in sampleWordList:
        print("�����J�bsampleWordList��\n")
    else:
        print("�����J���bsampleWordList��\n")