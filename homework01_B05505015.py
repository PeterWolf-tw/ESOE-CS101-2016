

file = open("sample.txt","r")
text = file.read()
file.close()

# HW 1-1
text1 = text.replace("\n"," ")
text2 = text1.replace("?"," ")
text = text2.split(" ")
sampleWordList=[]
for h in text:
    if len(h)>=5:
        sampleWordList.append(h)
        
    else:
        None 
print(sampleWordList)


# HW 1-2
a=0


while a<100000 :
    key = input("please key in a word more than five letters : ")
    if len(key) < 5:
        print("Not more than five letters \n")
        a=a+1
    elif key in sampleWordList:
        print("It is in the sampleWordList.\n")
    else:
        print("Not in sampleWordList.\n")
