samplefile=open(r'C:\Users\user\Desktop\sample.txt')
sampletext=samplefile.read()
samplefile.close()

unwanted=['"','.',',','?','\n','-']
for e in unwanted:
    newsampletext=sampletext.replace(e,"")
textlist=newsampletext.split(" ")

samplewWordList=[]
for word in textlist:
    if len(word)>5:
        sampleWordList.append(word)
    else:
        Pass
print(sampleWordList)

count=0
test=input("Please enter a word more than 5 letters:")
while count<10000:
    if len(test)>5:
        if test in sampleWordList
            print("The word is in sampleWordList."):
            count=count+1
        else:
            print("The word is not in sampleWordList.")
            count=count+1
    else:
        print("The word is too short!")
        count=count+1


        



