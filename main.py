'''

Exercise 8b:

Which is the last word, alphabetically, in a text file?

'''

file = open("text.txt","r")
article = sorted(file.read().split(' '))
print(article[-1])
