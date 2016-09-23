'''
=============================================================================
 |   Assignment:  HomeWork01
 |
 |       Author:  Chiaosung Yang(楊喬松)
 |     Language:  Python 3.5
 |        Class:  Introduction to Computer and Programming(1)
 |   Instructor:  CHIEN-KANG HUANG
 |     Due Date:  09.26.2016
 |
 +-----------------------------------------------------------------------------
 |
 |  Description:  DESCRIBE THE PROBLEM THAT THIS PROGRAM WAS WRITTEN TO
 |      SOLVE.
 |
 |        Input:  sample.txt, key words
 |
 |       Output:  (1-1)Words with more than five chars. (1-2)Check if the word  
 |                keyed in is in the sampleWordList.
 |
 |
 |   Known Bugs:  Not appliable by using Python 2.x.x
 +-----------------------------------------------------------------------------
 |  Update Log: 09.23.2016 First Version
 *============================================================================

'''
import string

file = open("sample.txt","r")
text = file.read()
file.close()
table = str.maketrans("\n"," ",string.punctuation) #make trans table
text = text.translate(table)
table = str.maketrans("","",string.digits) #make trans table
text = text.translate(table)
text_sp = text.split(" ") # divide words into a list

wordCount = len(text_sp);
sampleWordList = [] #to store the words that have more than five chars

for n in range(1, wordCount):
	if len(text_sp[n]) >= 5:
		sampleWordList.append(text_sp[n])

print(sampleWordList)# HW 1-1

while True:# HW 1-2
	key = input("Please key in the word : ")
	if len(key) < 5:
		print("Please key in the word with more than five characters\n")
		continue
	if key in sampleWordList:
		print("The word is in the sampleWordList.\n")
	else:
		print("The word is NOT in the sampleWordList.\n")