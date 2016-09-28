file=open("./sample.txt","r")
text=file.read()
file.close()
samplewordlist=[]
text=text.replace("?","")
text=text.replace(".","")
text=text.replace("\"","")
text=text.replace("-","") 
text=text.replace("\n"," ") 
text=text.replace(",","") 
text=text.replace("2000th","2,000th") 
textlist=text.split(" ")
for word in textlist:
    if len(word)>=5:
        samplewordlist.append(word)
print("====================================")
print(samplewordlist)
print("====================================")

checkword=input("Please input your more than five alphabets text here: ")
i=0
e=0
while i<len(samplewordlist):
    if samplewordlist[i] == checkword:
        e=e+1
        break
    else:
        i=i+1
    
if(e>0):
    print("The word does exist in the samplewordlist")

else:
    print("The word does NOT exist in the wordlist")


