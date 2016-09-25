
#1-1
<<<<<<< HEAD
Sfile=open("./sample.txt","r")
Sfiletext=Sfile.read()

=======
S=open("./sample.txt","r")
Stext=S.read()
S.close()
Marks=['?','-','.','"',"\n"]
for e in Marks:
    Stext=Stext.replace(e," ")
Stext=Stext.replace(',',"")

WordList=Stext.split(" ")
sampleWordList=[]
for h in WordList:
    if len(h)>5:
        sampleWordList.append(h)
    else:
        None
print(sampleWordList)
>>>>>>> 3b29bb2c6e956cce30fb450c01c16d882a98d306
