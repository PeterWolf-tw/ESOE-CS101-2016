samplefile = open("./sample.txt","r")
sampletext = samplefile.read()


print (str(sampletext) )

samplefile.close()


mark = ["!","?",".",",","'","{","}","[","]","..."]


for n in mark:
    turestory = sampletext.replace(n," ")


print (turestory)

    




