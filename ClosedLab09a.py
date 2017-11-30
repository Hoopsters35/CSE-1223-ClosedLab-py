def getNumDigits():
	dig = int(input('Please enter the number of digits to be stored: '))
	while dig < 0:
		print("ERROR - digits stored must be >= 0\n")
		dig = int(input('Please enter the number of digits to be stored: '))
	return dig
	
def getDigits(arr):
	for i in range(len(arr)):
		print('Enter integer', i)
		arr[i] = int(input())
	return arr
		
numD = getNumDigits()
if numD > 0:
	list = [None] * numD
	list = getDigits(list)
	print('\nThe contents of your array:')
	print('Number of digits in array: ', len(list))
	print('Digits in array:', str(list).replace(",", "").replace("[","").replace("]",""))
print('No digits to sort? Goodbye!')
