inp = input('Enter a string: ')
while inp:
	if inp == inp[::-1]:
		print(inp, 'is a palindrome.\n')
	else:
		print(inp, 'is NOT a palindrome.\n')
	inp = input('Enter a string: ')
print('Empty line read - Goodbye!')