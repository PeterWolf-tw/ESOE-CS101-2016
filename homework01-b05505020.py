samplefile = open("./sample.txt","r")
sampletext = samplefile.read()




mark = [".","?"]

for n in mark:
    story1 = sampletext.replace(n," ")
    
#story2 = story1.split(" ")


print (story1)

    


samplefile.close()
