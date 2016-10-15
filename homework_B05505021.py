
#計概作業1-1

f=open('sample.txt','r')
s=f.read()
sampleWordList=[]
m=['0','1','2',',','-','?','.','"']

#刪掉數字與標點符號
for e in m:
    s=s.replace(e," ")
s_list=s.split(" ")

#把字放進list
for w in s_list:
    if len(w) > 5:
        sampleWordList.append(w)
print(sampleWordList)

#計概作業1-2

while True:
    englishword = input("請輸入一個五個字母以上的英文字")
   
    if englishword in sampleWordList:
        print("這個字有在列表裡喔喔喔喔")
    else:
        print("這個字沒在列表裡喔87")
