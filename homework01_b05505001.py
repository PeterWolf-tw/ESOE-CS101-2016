#part1.1
file = open("ESOE-CS101-2016/sample.txt", encoding='utf-8-sig')
replace = file.read().replace("\n"," ").replace("?","").replace(".","").replace("-","")
sample = replace.split(" ")
sampleWordList = []
for n in range(0,len(sample)):
    if len(sample[n]) > 5 :
        sampleWordList.append(sample[n])

print(sampleWordList)
#part1.2
asking = 1

while asking > 0:
    test = input()
    if test in sampleWordList:
        print(test + " is in sampleWordList")
    else:
        print(test + " is not in sampleWordList")

