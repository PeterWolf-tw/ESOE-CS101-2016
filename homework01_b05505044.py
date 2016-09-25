# Homework1-1



 
work = open("./sample.txt","r")
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

 