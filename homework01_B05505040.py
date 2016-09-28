import re
#student ID: B05505040
#python 2.7.12
#part 1-1
sample = open("./sample.txt", "r")
sample_read = sample.read()


sample_read_nonewline = sample_read.replace("\n"," ") #replace newline '\n' with spaces ' '


alphabet = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')

sample_read_alpha = ''.join(filter(alphabet.__contains__,
sample_read_nonewline)) #this will filter out every character that is not of the alphabet

sample_words = sample_read_alpha.split(" ")


sampleWordList = []
for x in range(0, len(sample_words)):
    if len(sample_words[x]) > 5:
        sampleWordList.append(sample_words[x])
        x = x + 1
    else:
        x = x + 1


print "the list 'sampleWordList' has the following words:\n "
for word_sWL in sampleWordList:
    print word_sWL

#part 1-2

print "\n\n"
print "This script sees if the word you type is on the list 'sampleWordList'."
print "It only accepts letters, not special characters or spaces, except for the",
print "command to close the script."
print "If you want to close the program, please type the following:",
print "'I want to exit'"
print "Type a word bigger than 5 letters: "

while True:
    userword = raw_input("> ")
    if userword == "I want to exit":
        print "Script closing..."
        break
    if not re.match("^[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy]*$", userword):
#this won't allow any input that is not from the alphabet.
        print "Error! Special characters and spaces are not allowed."
        print "Please try again:"
    elif len(userword) > 5:
        if userword in sampleWordList:
            print "The word '%s' you entered is on the list." % userword
        else:
            print "The word '%s' you entered is not on the list," % userword
            print "please try again:"
    else:
        print "The word '%s' you entered is smaller or equal to 5 letters," % userword
        print "please try again:"
