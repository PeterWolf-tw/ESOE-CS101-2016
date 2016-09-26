s=open("C:/Users/user/Desktop/sample.txt","r")
sample=s.read()
s.close()
a=['"','(',')','?','!',',','.','\n','[',']','{','}',';',':','-',"'"]
for x in a:
    sample=sample.replace(x,'')
samplelist=sample.split(" ")
samplewordlist=[]
for n in samplelist:
    if len(n)>5:
        samplewordlist.append(n)
    else:
        pass
print(samplewordlist)

while True:
    y=input("enter a word more than five letters:")
    if y in samplewordlist:
        print("in samplewordlist. :)")
    elif len(y)<=5:
        print('you have to enter "more than five" letters!!!')
    else:
        print("sorry, not in samplewordlist.")