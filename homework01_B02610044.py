Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #撰寫作業1-1
#打開sample.txt
TheOpenedText = open("./sample.txt","r")

#將其改成人看的懂的文字
TheOpenedTextToRead = TheOpened.read()

#列出要去掉的標點與數字
StringNotNeed = ["?","2","0","-","'"'",".","1"]

#把它們去掉並列表
for Bye in StringNotNeed:
  TheOpenedTextToRead = TheOpenedTextToRead.replace(Bye,"  ")
  List = TheOpenedTextToRead.split(" ")
  
#產生sampleWorldList
for Word in List:
  if len(Word) > 5:
    sampleWorldList.append(word)
Print(sampleWorldList)
