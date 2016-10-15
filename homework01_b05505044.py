# Homework1-1



 
work = open("C:/Users/user/Desktop/sample.txt","r")
watch = work.read()
work.close()

sampleWordList = []


watch = watch.replace("?","")
watch = watch.replace("-","")
watch = watch.replace(".","")
watch = watch.replace(",","")
watch = watch.replace("\n"," ")

result= watch.split(" ")

for n in result:
    if len(n) >= 5:
        sampleWordList.append(n)

print(sampleWordList)
print("=================")

#HW 1-2
while True:
    x=input('please input a word >= 5 letters:')
    if x in sampleWordList:
        print('have this word')
    else:
        print("don't have this word")

 