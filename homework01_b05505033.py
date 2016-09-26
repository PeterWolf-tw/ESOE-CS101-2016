#read the file from the sample.txt
wordfile=open("C:\\Users\翁震軒\Desktop\sample.txt","r", encoding="utf8")
wordtext=wordfile.read()
#killing the marks
wordtext1=wordtext.replace("."," ")
wordtext2=wordtext1.replace("?"," ")
wordtext3=wordtext2.replace('"'," ")
#define an empty list
sampleWordList=[""]
#change the string into a list
sampleWord=wordtext3.split()
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
        print("Please enter more that 5 letters")
        whilecount=whilecount+1
#if the user got it
    elif ans in sampleWordList:
        print( "you keyed in "+ans)
        whilecount=whilecount+1
#if the word isnt on the list
    else:
        print("sorry not found")
        whilecount=whilecount+1
#change log
         # added the "kill mark" code
