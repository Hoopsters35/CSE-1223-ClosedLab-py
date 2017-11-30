def getWordCount(input):
	numWords = 1
	while " " in input:
		numWords += 1
		input = input[input.index(' ') + 1: len(input)]
	return numWords
	
string = input('Enter a string: ')
while not string:
	print('ERROR - string must not be empty\n')
	string = input('Enter a string: ')
print(getWordCount(string))
print('Your string has', str(getWordCount(string)), 'words in it.')