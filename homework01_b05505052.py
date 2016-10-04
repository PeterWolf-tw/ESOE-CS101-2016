


#1-1
sampleFile = open("sample.txt", "r")
rsampleFile = sampleFile.read()
pun=[',','?','0','1','2','-','/','\n','"','.' ]
for a in pun:
    rsampleFile=rsampleFile.replace(a," ")#蝘駁�璅��蝚西����銵�
wordList = rsampleFile.split(" ")
sampleCounter = 0 # 韏瑕���
sampleWordList = [ ]
while sampleCounter < len(wordList): # 蝯�迫璇�辣
 if len(wordList[sampleCounter]) > 5:
  sampleWordList.append(wordList[sampleCounter])
  sampleCounter = sampleCounter + 1 # ���蝯�迫璇�辣���餈��甇�
 else:
  sampleCounter = sampleCounter + 1
  
print(sampleWordList)  



#1-2

num = 1
while num==1:
 quest = input("隢�撓�乩����瘥�誑銝���望�摮�)
 if len(quest)<=5:
  print("摮��銝�雲")
  
 elif quest in wordList:
  print("皜��鋆⊥�����桀�")
  
 else: 
  print("皜��鋆⊥�������摮�)
 
