#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#前兩行請養成習慣宣告程式種類以及編碼



#file = open('/Users/candy/Downloads/sample.txt', 'r')
file = open("./sample.txt", "r")
#用相對路徑的適用性會更廣一些。
samplestring = file.read()
sampleWordList = []
samplestring=samplestring.replace('?', ' ')
samplestring=samplestring.replace('.', ' ')
samplestring=samplestring.replace('2', ' ')
samplestring=samplestring.replace(',', ' ')
samplestring=samplestring.replace('0', ' ')
samplestring=samplestring.replace('-', ' ')
samplestring=samplestring.replace('1', ' ')
samplestring=samplestring.replace('\n', ' ')
samplestring=samplestring.replace('"', ' ')


for word in samplestring.split(' '):
    if len(word) > 5:
        sampleWordList.append(word)
print(sampleWordList)

print('     ')
print('=======This is a demarcation=======')
print('     ')

count = 7
while count > 0:
    w = input('Please input any English word that has over five letters^_^  ')
    print('You have only', count, '-1', 'times left!')
    count -= 1
    if w in sampleWordList:
        print('Congratulations^^ The word you input is in the sampleWordList!')
        print('     ')
    if w not in sampleWordList and len(w) > 5:
            print('Oh no! The word you input is not in the sampleWordList! Please try again!')
            print('     ')
    if len(w) <= 5:
            print('Hey! You have to input word that has over five letters= =')
            print('     ')
while count < 1:
    print('See you next time!')
    break
