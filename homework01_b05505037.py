# B05505037
# HW1

# HW1-1

file = open("./sample.txt","r")
read_file = file.read()
read_file = file.lower()
file.close()

sampleWordList = []
read_file = read_file.replace("2,000th","2000th")
puntuationList = [".",",","!","?","-","\'","\"","\n"]
for puntuation in puntuationList:
    read_file = read_file.replace(puntuation," ")

wordList = read_file.split(" ")
for word in wordList:
    if len(word)>5:
        sampleWordList.append(word)

print(sampleWordList)

# HW1-2

inputword = input("Please input a word which includes more than 5 letters.")

if len(inputword) <=5:
    print("You should input a word which includes more than 5 letters.")

else:
    number = 0
    while number < len(sampleWordList):
        if sampleWordList[number] == inputword:
            result = True
        else:
            result = False
        number = number+1

if result == True:
    print(inputword," exists in sampleWordList.")
else:
    print(inputword," does not exist in sampleWordList.")