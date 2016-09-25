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
'''print (text)'''

textList=text.split(" ")

for word1 in textList:
	if len(word1)>=5:
		sampleWordList.append(word1)
print ("================sampleWordList==================")
print sampleWordList
print ("================================================")

userWord=raw_input("Please input a word:")

result=False
i=0
while i<len(sampleWordList):
	if sampleWordList[i] == userWord:
		result=True
	i=i+1
		
if result==True:
	print("The word you input exists!")
else:
	print("The word you input do NOT exists!")
