f=open("./sample.txt","r")
t=f.read()
s2=t.replace("."," ") 
s3=s2.replace(","," ")
s4=s3.replace("-"," ")
s5=s4.replace("!"," ")
s6=s5.replace("?"," ")
s7=s6.replace("\n"," ")
t2=s7.split(" ")

sampleWordList = [ ]

for x in t2:
  if len(x) > 5:
    sampleWordList.append(x)
print(sampleWordList)

z=500
while z<1000:
  w= input('please enter a word!')
  if w in  sampleWordList:
    z+=1
    print('exist')
  else:
    z-=1
    print('not exist')

 
   



