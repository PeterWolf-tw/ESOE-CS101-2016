#帳號未授權,借同學帳號上傳
word=input("請輪入一個字串(表示結果為['字母',出現機率])：")
lenth=len(word)
wordlist=list(word)
worddictionary={} #建立儲存字元的資料庫

c=0
for n in wordlist:
    if n in worddictionary:
        worddictionary[n]=worddictionary[n]+1 #因為字元在資料庫內，直接增加字元出現的次數
    else:
        worddictionary[n]=1 #字元不在資料庫內，將字元加入資料庫，並將出現的次數設為1

wordlist2=list(worddictionary.keys()) #取出資料庫中的字元資料
sequencelist=[]
resultlist=[]
i=0
j=0
for nu in wordlist2:
    if worddictionary[nu]>0:
        sequencelist.append(((worddictionary[nu]/lenth),wordlist2[i])) #前者計算出現的機率，後者記錄字元
        i=i+1

sequencelist.sort(reverse=True) #換成機率由高到低的排列方式

while j<i:
    resultlist.append([sequencelist[j][1],sequencelist[j][0]]) #調整成前者為字元，後者為出現的機率的形式
    print(resultlist[j])
    j=j+1
