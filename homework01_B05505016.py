file =open("D:/sample.txt","r")
a =file.read()
file.close()

#HW1-1

b =a.replace("\n"," ")
c =b.replace(","," ")
d =c.replace("."," ")
f =d.replace("-"," ")
g =f.replace("?"," ")
h =g.replace("\""," ")
i =h.split(" ")

sampleWordList = [ ]

for j in i:
    if len(j)>=5:
        sampleWordList.append(j)
        
print(sampleWordList)

#HW1-2

k =0

while k<10000:
    key =input("輸入一個超過5個字母的單字")
    if key in sampleWordList:
        print("這個單字有在文章裡喔!!")
        k =k+1
    
    elif len(key)<5:
        print("請輸入5個單字以上的單字")
        
    else:
        print("這單字沒在文章裡!")
    