#1-1
file=open("sample.txt","r")
fil=file.read()
file.close()
m=['?',',','.','-','\n','"']
for element in m:
    fil=fil.replace(element," ")
    filee=fil.split(" ")
sampleWordList=[]
print("sampleWordList:")
for word in filee:
    if len(word)>5:
        sampleWordList.append(word)
for x in sampleWordList:
        print(x)
#1-2
while True:
    word=input("Please enter a word with more than 5 letters:")
    if len(word) > 5:
        if word in sampleWordList:
            print("Congratulations, this word is in the sampleWordList.")
        else:
            print("Sorry, the word you enter is not in the sampleWordList. Please try again!")


        
    

