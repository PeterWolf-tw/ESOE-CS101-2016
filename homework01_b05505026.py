#=======================================homework1-1

#impot sample.txt
F=open("sample.txt","r")
FF=F.read()
F.close()

#delete invalid characters
FF=FF.replace("?"," ")
FF=FF.replace(","," ")
FF=FF.replace("2"," ")
FF=FF.replace("0"," ")
FF=FF.replace("1"," ")
FF=FF.replace("."," ")
FF=FF.replace("-"," ")
FF=FF.replace("\n"," ")
FF=FF.replace("\""," ")

FFlist=FF.split(" ")

sampleWordList=[]

for i in FFlist:
    if len(i) >5 :
      sampleWordList+=[i]

#Output the list      
print("sampleWordList :")      
print(sampleWordList)
print("\n")



#=======================================homework1-2

#Use x as the condition
x=1

#Use loop to select the correct word
while x==1:
    word=input("Please enter a word containing 5 letter at least.")
    word=str(word)
    if len(word) <5:
        print("You should type more letter.")
        x=1
    else:
        if (word in sampleWordList)==1:
            print("The word is in the sampleWordList.")
            print("Finish")
            x=2
        else:
            print("The word isn't in the sampleWordList.")
            x=1
            