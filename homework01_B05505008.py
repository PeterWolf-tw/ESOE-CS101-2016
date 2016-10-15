# encoding: utf-8
# B05505008 python作業一
fileopen = open("/Users/wayne/Desktop/homework.py/sample.txt","r")
punctuation = ["," ,".","\n","\"","?","2","0"]
data_1 = fileopen.read()

for element in punctuation:
    data_1 = data_1.replace(element,"  ")

data_2 = data_1.split(" ")
sampleWordList = []

for word in data_2:
    if len(word) > 5:
        sampleWordList.append(word)

print(sampleWordList)
fileopen.close()

print("讓輸入任何五個字母以上的英文字。")
key = raw_input()
a = 0
counter = 0
while counter < len(sampleWordList):
    if sampleWordList[counter] == key:
        print("這個字存在於列表sampleWordList內")
        a = 1
    counter = counter +1

if a == 0:
    print("這個字不存在於列表sampleWordList內")
