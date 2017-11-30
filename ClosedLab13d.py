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

def getValidSub(word):
	subs = input('Enter a substring to delete(empty to stop): ')
	while (subs not in word) and subs:
		print('Error: substring must be found in', word)
		subs = input('Enter a substring to delete(empty to stop): ')
	return subs

word = input('Enter a word (empty to quit): ')
while word:
	subs = getValidSub(word)
	while subs:
		word = word[:word.index(subs)] + word[word.index(subs) + len(subs):]
		print('Current word', word)
		subs = getValidSub(word)
	print('Final word:', word)
	word = input('\nEnter a word (empty to quit): ')
print('Goodbye!')