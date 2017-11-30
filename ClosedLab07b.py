def getWordCount(input):
	numWords = 1
	while " " in input:
		numWords += 1
		input = input[input.index(' ') + 1: len(input)]
	return numWords
	
def getFirstWord(input):
	if ' ' in input:
		input = input[:input.index(' ')]
	return input
	
def getWord(input, n):
	if n < 1 or n > getWordCount(input):
		return ""
	for i in range(n -1):
		input = input[input.index(' ') + 1: len(input)]
	if n < getWordCount(input):
		input = input[:input.index(' ')]
		return input
	return input
		
		
	
string = input('Enter a string: ')
while not string:
	print('ERROR - string must not be empty\n')
	string = input('Enter a string: ')
print(getWordCount(string))
print('Your string has', str(getWordCount(string)), 'words in it.')
print('The first word is:', getFirstWord(string))
if getWordCount(string) > 1:
	nth = int(input('Which number word would you like to see? '))
	print('Word number', str(nth), 'is', getWord(string, nth))