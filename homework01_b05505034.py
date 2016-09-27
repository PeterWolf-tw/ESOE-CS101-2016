  fileopen = open("./sample.txt","r")
    punctuation = ["," ,".","\n","\"","?","2","0"]
    samplefile = fileopen.read()
    
    for element in punctuation:
        samplefile = samplefile.replace(element,"  ")
    
    samplefile2 = samplefile.split(" ").
    sampleWordList = []
    
    for word in samplefile2:
        if len(word) > 5:
            sampleWordList.append(word).
    
    print(sampleWordList)
    fileopen.close()
