import re
#student ID: B05505040
#This version:python 3.5.2
#old version:python 2.7.12
#part 1-1
sampleFile = open("./sample.txt", "r")
sampleRead = sampleFile.read()

letterString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
letterList = []

for i in range(len(letterString)):
    letterList += letterString[i]

sampleAlpha = ""
for y in sampleRead:
    if y in letterList:
        sampleAlpha += y
    elif y == "\n":
        sampleAlpha += " "

sampleWords = sampleAlpha.split(" ")
for y in sampleWords:
    if re.match("^[ ]*$", y):
        sampleWords.remove(y)

sampleWordList = []
for y in sampleWords:
    if len(y) > 5:
        sampleWordList.append(y)


for y in sampleWordList:
    print(y)

#part 1-2
print("Please type a word bigger than 5 letters")
print("To exit the program type'I want to exit'.")
while True:
    userword = str(input())
    if userword == "I want to exit":
        print("Script closing...")
        break
    if not re.match("^[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy]*$", userword):
#this won't allow any input that is not from the alphabet.
        print("Error! Special characters and spaces are not allowed.")
        print("Please try again:")
    elif len(userword) > 5:
        if userword in sampleWordList:
            print("The word '" + userword + "' is on the list.")
        else:
            print("The word '" + userword + "' is not on the list,")
            print("please try again:")
    else:
        print("The word '" + userword + "' is smaller or equal to 5 letters,")
        print("please try again:")
