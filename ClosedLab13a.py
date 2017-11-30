def removeSpaces(word):
	newWord = ""
	for i in word:
		if i != " ":
			newWord += i
	return newWord

word = input('Enter a word to de-space: ')
while word:
	print('Word without spaces: ', removeSpaces(word))
	word = input('Enter a word to de-space: ')
print('Goodbye!')