#student ID: B05505040
#part 1-1
print "\n\n"
sample = open("./sample.txt", "r")
sample_read = sample.read()


sample_read_nonewline = sample_read.replace("\n"," ") #replace newline with spaces

alphabet = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')

sample_read_alpha = ''.join(filter(alphabet.__contains__,
sample_read_nonewline)) #this will filter out every character that is not of the alphabet

sample_words = sample_read_alpha.split(" ") #this will make a list consisting
# of words in the sample


sampleWordList = []
for x in range(0, len(sample_words)):
    if len(sample_words[x]) > 5:
        sampleWordList.append(sample_words[x])
        x = x + 1
    else:
        x = x + 1

y = 0
print "the list 'sampleWordList' has the following words:\n "
for y in range(y, len(sampleWordList)):
    print sampleWordList[y]
    y = y + 1

#part 1-2

print "\n\n"
print "This script sees if the word you type is on the list 'sampleWordList'."
print "Type a word bigger than 5 letters: "
n = 0
while True:
    userword = raw_input("> ")
    if len(userword) > 5:
        if userword not in sampleWordList: #this checks if the word is not on the list
            print "The word you entered is not on the list, please try again."
        else: #the only other possible case, is if the word is on the list
            print "The word you entered is on the list."
            print "program exiting"
            break
    else:
        print "The word you entered is smaller or equal to 5 letters, please try again."
