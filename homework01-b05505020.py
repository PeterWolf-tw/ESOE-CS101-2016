samplefile = open("./sample.txt","r")
sampletext = samplefile.read()



finallist = []
mark = [".","?","(",")",",","!","\"","/",]

for n in mark:
    sampletext = sampletext.replace(n," ")
    
story = sampletext.split(" ")


#print (story)




for word in story:
    if len(word) >= 5:
        finallist.append(word)



python = 0

while python == 0:
    inpu = input("打個字巴")
    if len(inpu) < 5:
        print("打個超過五個英文單字的單字巴，別怪我剛剛沒告訴你")
    elif inpu in finallist:
        print("Good job, 你打出了finallist的字耶")
    else:
        print("你亂打，你可以回家了")

    

samplefile.close()
