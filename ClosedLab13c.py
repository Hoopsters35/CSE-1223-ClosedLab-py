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

word = input('Enter a word (empty to quit): ')
while word:
	index = int(input('Enter an index to remove(-1 to quit): '))
	while index >= 0:
		word = word[:index] + word[index+1:]
		print('Current word', word)
		index = int(input('Enter an index to remove(-1 to quit): '))
	print('Final word:', word)
	word = input('\nEnter a word (empty to quit): ')
print('Goodbye!')