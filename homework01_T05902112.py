


hwfile=open("E:/sample.txt","r")
t=hwfile.read()
hwfile.close()

sampleWordList=[]
allkindsofmark = ["0","1","2","3","4","5","6","7","8","9",".",",","-","!","?","\"","\n"]
for rm in allkindsofmark:
    t=t.replace(rm," ")

t=t.split(" ")
for word in t:
    if len( word )>5:
        sampleWordList.append( word )

print(sampleWordList)



while True:
    enter = input("ݔ��5����ĸ���ϵĆ���")
    if len ( enter ) < 5:
        print("���ֱ�횴��5����ĸ!")
        
    elif enter in sampleWordList:
        print(enter,"Cool! Your word is in the sampleWordList!")
        
    else:
        print("Sorry, Your word is not in the sampleWordList!")
