def removeSpaces(word):
	newWord = ""
	for i in word:
		if i != " ":
			newWord += i
	return newWord

def expandString(word):
	newWord = ""
	for i in range(len(word)):
		newWord += (word[i] * i)
	return newWord

word = input('Enter a word to expand: ')
while word:
	print('Word expanded: ', expandString(word))
	word = input('Enter a word to expand: ')
print('Goodbye!')