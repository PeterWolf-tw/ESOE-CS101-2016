#B05505024
file=open('/Users/Raymond/Documents/sample.txt')
text=file.read()
file.close
file=open('/Users/Raymond/Documents/sample.txt')
context=file.read()
file.close

SymbolList=[',','.','!','?','#','$','%','&','-','"','\n','0','1','2','3','4','5','6','7','8','9']
text=text.lower()

for sym in SymbolList:
    text=text.replace(sym,' ')
    
wordsnletters=text.split()

sampleWordList=[]
for letters in wordsnletters:
    if len(letters)>4:
        sampleWordList.append(letters)
      
Sentences=context.split('\n')

print(sampleWordList)

while True:
    answer=input('See if a word is in the passage!\n')
    if len(answer)<5:
        print('Please enter a word with five letters or more!\n')
    else:
        if answer in sampleWordList:
            print('The word '+'"'+answer+'"'+' is in the passage.')
            for S in Sentences:
                if answer in S:
                    print('"'+S+'"''\n')
            
        else:
            print('The word',answer,'is NOT in the passage.\n')
