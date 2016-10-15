'''
=========================

Title: Homework01
Author: Tim Bian
Language: Python 3

=========================
'''

# 1-1

file = open('./sample.txt', 'r')
text = file.read()
file.close()

symbols = ['?', '.', ',', '"', '-']

for i in symbols:
    text = text.replace(i, '')
text = text.replace('\n', ' ')

list = text.split(' ')  
sampleWordList = [] # store the words that are more than 5 characters

for word in list:
    if len(word) > 5: # not sure whether >5 or >=5 !!!
        sampleWordList.append(word)
print('Following are the words that are more than 5 characters...')        
print(sampleWordList)


# 1-2

while True:
    word = input('Please enter a word...\n')
    if len(word) <= 5:
        print('The word must be more than 5 characters!!!')
    else:
        print('"' + word + '"', end=' ')
        if word in sampleWordList:
            print('is in the list!')
        else:
            print('is NOT found!')