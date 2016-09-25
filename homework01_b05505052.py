#1-1
sampleFile = open("sample.txt", "r")
rsampleFile = sampleFile.read()
pun=[',','?','0','1','2','-','/','\n','"','.' ]
for a in pun:
    rsampleFile=rsampleFile.replace(a," ")#移除標點符號與換行
wordList = rsampleFile.split(" ")
sampleCounter = 0 # 起始值
sampleWordList = [ ]
while sampleCounter < len(wordList): # 終止條件
 if len(wordList[sampleCounter]) > 5:
  sampleWordList.append(wordList[sampleCounter])
  sampleCounter = sampleCounter + 1 # 向「終止條件」靠近一步
 else:
  sampleCounter = sampleCounter + 1
  
print(sampleWordList)  



#1-2

num = 1
while num==1:
 quest = input("請輸入五個字母以上的英文字")
 if len(quest)<=5:
  print("字數不足")
  
 elif quest in wordList:
  print("清單裡有這個單字")
  
 else: 
  print("清單裡沒有這個單字")
 
