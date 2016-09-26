#B05505041

sampleFile = open("./sample.txt", "r")
sampleRead = sampleFile.read()
m = ['?','\n', ',','-','""','.','!','0','1','2','3','4','5','6','7','8','9']
#for element in m:
#     wordList = sampleRead.replace("m"," ")
print sampleRead

for x in m:
    sampleRead = sampleRead.replace(x, " ")
wordList = sampleRead.split(" ")

wordSampleList = []
for w in wordList:
    if len(w) > 5:
        wordSampleList.append(w)

for w in wordSampleList:
    print w

print("Please input a word with more than 5 digits.")

while True:
    userword = raw_input("> ")
    if len(userword) > 5:
        if userword in wordSampleList:
            print("Nice job! This word is on the list.")
        else:
            print("Sorry, the word you use is not on the list. Please, try again.")
    else:
        print("Sorry. Your word is less or equal to five digits. Please, try again with a different word.")
