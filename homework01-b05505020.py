samplefile = open("./sample.txt","r")
sampletext = samplefile.read()




mark = [".","?","(",")",",","!","\"","/",]

for n in mark:
    sampletext = sampletext.replace(n," ")
    
story = sampletext.split(" ")


print (story)

    


samplefile.close()
