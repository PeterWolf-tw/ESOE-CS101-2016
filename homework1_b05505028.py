#file.py
f=open("./sample.txt","r")
b=f.read()
f.close()
"""------------------------------------讀取資料"""

k=[]
str(k)
for i in range(0,len(b),1):
    k.append(b[i])#將字串轉為陣列   
    if(ord(k[i])<ord('A')or ord(k[i])>ord('z')):
        k[i]=' '#將非大小寫的符號換為空白
m=''
a=m.join(k)   #將陣列轉回字串
l=[]
l=a.split()#拆為字彙
sampleWordList =[]#列表
for i in range(0,len(l),1):
    if len(l[i])>=5:
        sampleWordList.append(l[i])#將自述多於5的字丟入列表
print (sampleWordList )
"""----------------------------------列表"""
boo=False
while(True):
    s=input('Please input the word more then five letters\n')
    if len(s)<5:
    	print ("your input is lesser than five letters")
    	continue
    if(s==''):
        break
    boo=False#確定是否有相同的字彚在文章中
    for i in range (0,len(sampleWordList ),1):
        if s==sampleWordList [i]:#找到
            print ('The word exists in the list')
            boo=True
            break#直接脫離迴圈
    if boo==False:#全部沒找到
        print ('The word doesn\'t exist in the list')
"""---------------------------------查詢有無(while迴圈)"""