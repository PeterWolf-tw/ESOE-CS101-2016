file = open("./sample.txt","r")
text = file.read()
file.close()
text = text.replace("?","")
text = text.replace(",","")
text = text.replace("-","")
text = text.replace("\"","")
text = text.replace(".","")
text = text.replace("2000th","2,000th")
text = text.replace("\n"," ")

samplewordlist=[]
wordlist = text.split(" ")
for word in wordlist:
    if len(word)>5:
     samplewordlist.append(word)
print ("samplewordlist:")
print (samplewordlist)

samplewordlist1=[]
newwordlist1=[]
wordlist1 = text.lower()
newwordlist = wordlist1.split(" ")
for word in newwordlist:
    if len(word)>5:
     newwordlist1.append(word)



userword = input("Please enter a word which contains more than five characters:").lower()

i = 0
x = 0
while i < len(samplewordlist) :
     
    
    if len(userword)<=5:
        x= 2
        break
    elif userword == newwordlist1[i]:
        x = 1
        break
    i = i+1
if x==2:
    print("U should enter a word with more than five characters.")

if x==1:
    print ("The word is also in the article!")
    
if x==0:
    print ("The word is not in the article!")
    
   

    
