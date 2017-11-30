letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getText():
	inp = input('Enter your text to encrypt (!!! to quit): ')
	while not inp:
		print('ERROR: String can not be empty')
		inp = input('Enter your text to encrypt (!!! to quit): ')
	return inp
	
def getShift():
	shift = int(input('Enter amount to shift text by: '))
	while shift < 0 or shift > 26:
		print('ERROR: Shift must be between 0 and 26')
		shift = int(input('Enter amount to shift text by: '))
	return shift
	
def rot13(string):
	out = ""
	for l in string:
		if l.upper() in letters:
			if letters.index(l.upper()) <= 12:
				out += letters[letters.index(l.upper()) + 13: letters.index(l.upper()) + 14]
				
			elif letters.index(l.upper()) >= 13:
				out += letters[letters.index(l.upper()) - 13: letters.index(l.upper()) - 12]
				
	return out
	
def shiftMessage (string, n):
	out = ""
	for i in string:
		if i.upper() in letters:
			if letters.index(i.upper()) <= 25 - n:
				out += letters[letters.index(i.upper()) + n: letters.index(i.upper()) + n + 1]
			else:
				out += letters[letters.index(i.upper()) - n: letters.index(i.upper()) - n + 1]
	return out

def displayResults(inText, encText):
	l1 = "ORIGINAL:  " + inText
	l2 = "ENCRYPTED: " + encText
	print("+" + "-" * (len(l1) + 2) + "+")
	print("|", l1, "|")
	print("|", l2, "|")
	print("+" + "-" * (len(l2) + 2) + "+")
	
str = getText()
while not str == "!!!":
	n = getShift()
	encStr = shiftMessage(str, n)
	displayResults(str, encStr)
	str = getText()
print("Goodbye!")