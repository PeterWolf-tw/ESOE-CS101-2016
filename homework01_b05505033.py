#read the file from the sample.txt
wordfile=open("C:\\Users\翁震軒\Desktop\sample.txt","r", encoding="utf8")
wordtext=wordfile.read()
#define an empty list
sampleWordList=[""]
#change the string into list
sampleWord=wordtext.split()
#HW1-1
for sampleWordList1 in sampleWord:
    if len(sampleWordList1)>5:
        print(sampleWordList1)
#add the five or above letter words into the list
        sampleWordList.append(sampleWordList1)
#HW1-2
#loop starting
whilecount=1
while whilecount:
#user type in the word 
    ans=input("input= ")
#if the the word is lesser than five LETTERS
    if len(ans)<5:
        print("Error lesser that 5 letters")
        whilecount=whilecount+1
#if the word is'nt on the list
    elif ans in sampleWordList:
        print( "you keyed in "+ans)
        whilecount=whilecount+1
#if the user got it
    else:
        print("sorry not found")
