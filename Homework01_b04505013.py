'''
=============================================================================
 |   Assignment:  HomeWork01
 |
 |       Author:  Chiaosung Yang(楊喬松)
 |     Language:  Python 3.5
 |        Class:  Introduction to Computer and Programming(1)
 |   Instructor:  CHIEN-KANG HUANG
 |           TA:  PitaWolf
 |     Due Date:  09.26.2016
 |
 +-----------------------------------------------------------------------------
 |
 |  Description:  
 |			1-1: ( 完成者,本次作業分數 75 起計 )
 |			將 sample.txt 的內容長度超過 5 的詞彙加入一個名為
 |			讀取同目錄下名為 "sample.txt" 的純文字檔案。
 |			sampleWordList 的列表中並顯示出來。 
 |
 |			1-2:(完成者,本次作業分數 80 起計)
 |			做完以上動作以後,再加一個 while... 迴圈,讓使用者輸入任何五個 
 |			字母以上的英文字,然後告訴使用者剛才輸入的字,是否在 sampleWordList 裡!
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

sampleWordList = [] #to store the words that have more than five chars

file = open("./sample.txt","r")
text = file.read()
file.close()

#=============================================================================
# HW 1-1

#delete redundant chars and divide the words
table = str.maketrans("\n"," ",string.punctuation) #make trans table
text = text.translate(table) #replace the redundant words to null
table = str.maketrans("","",string.digits) #make trans table
text = text.translate(table) #replace the redundant words to null
text_sp = text.split(" ") # divide words into a list

wordCount = len(text_sp);
for n in range(1, wordCount):
	if len(text_sp[n]) >= 5:
		sampleWordList.append(text_sp[n])

print(sampleWordList)

#=============================================================================
# HW 1-2

while True:
	key = input("Please key in the word : ")
	if len(key) < 5:
		print("Please key in the word with more than five characters\n")
		continue
	if key in sampleWordList:
		print("The word is in the sampleWordList.\n")
	else:
		print("The word is NOT in the sampleWordList.\n")

#=============================================================================
#End of the program.
#=============================================================================