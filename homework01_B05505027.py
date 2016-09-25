Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
#Homework1-1-------------------------------------------------------

#讀取檔案並轉為可讀文字
f1=open("sample.txt","r")
f2=f1.read()
f1.close()

#刪除非必要符號並分割詞彙
f3=f2.replace("-"," ")
f3=f3.replace("."," ")
f3=f2.replace("?"," ")
f3=f3.replace(","," ")
f3=f3.replace("0"," ")
f3=f3.replace("1"," ")
f3=f3.replace("2"," ")
f3=f3.replace("\""," ")
f3=f3.replace("\n"," ")
f4=f3.split(" ")

#生成列表並篩選列表詞彙
sampleWordList=[]

end=len(f4)
n=0
while n<=end:
	if len(f4[n])>5:
		sampleWordList.append(f4[n])
		n+=1
	else:
		n+=1
#產出列表     
print(sampleWordList)

#Homework1-2-------------------------------------------------------

while:
word=input("please type a word with more than 5 letters.")#輸入詞彙
	if len(word)<5:#判定詞彙是否超過五個字
        print("lease type a word with more than 5 letters again.")
	else
        	if word in  sampleWordList:#判定詞彙是否存在列表裡
                print("this word exist in the list!")
        	else:
                print("this word doesn't exist in the list!")




