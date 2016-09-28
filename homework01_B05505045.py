1-1
ff=open("C:\sample.txt",'r')
f1=ff.read()
ff.close()


f2=f1.replace('.',' ')
f3=f2.replace(',',' ')
f4=f3.replace('-',' ')
f5=f4.replace('"',' ')
f6=f5.replace('\n',' ')
f7=f6.replace('?',' ')


fff=ff.split(' ')


for F in fff:
    if len(F)>5:
        sampleWordList.append(F)
        
        
print(sampleWordList)

1-2

while True:
    F=input('please input a word > 5 letters:')
    if F in sampleWordList:
        print('Victory!')
    eles:
        print('Nothing but error')
        
