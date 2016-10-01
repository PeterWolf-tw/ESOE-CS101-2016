file = open("./sample.txt","r")
text = file.read()
file.close()

sampleWordList = []
text = text.replace("?","")
text = text.replace(".","")
text = text.replace("\"","")
text = text.replace("-","") 
text = text.replace("\n"," ") 
text = text.replace(",","") 
text = text.replace("2000th","2,000th") 

textList=text.split(" ")

for word1 in textList:
	if len(word1)>5:
		sampleWordList.append(word1)
print ("================sampleWordList==================")
print (sampleWordList)
print ("================================================")

while True:
	while True:
		userWord=input("Please input a word > 5 letters:")
		if len(userWord)>5:
			break
		print("INPUT A WORD > 5 LETTERS!!!\n")

	result=False
	i=0
	while i<len(sampleWordList):
		if sampleWordList[i].lower() == userWord.lower():
			result=True
		i=i+1

	if result==True:
		print("The word you input EXISTS!\n")
	else:
		print("The word you input do NOT EXISTS!\n")
