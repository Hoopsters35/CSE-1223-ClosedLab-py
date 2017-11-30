def getNumDigits():
	dig = int(input('Please enter the number of digits to be stored: '))
	while dig < 0:
		print("ERROR - digits stored must be >= 0\n")
		dig = int(input('Please enter the number of digits to be stored: '))
	return dig
	
def selectionSort(digits):
	index = 0
	while index < len(digits) - 1:
		min = 500000000000
		for i in range(index, len(digits)):
			if digits[i] < min:
				min = digits[i]
				digits[i] = digits[index]
				digits[index] = min
				
		index += 1
		
	
def getDigits(arr):
	for i in range(len(arr)):
		print('Enter integer', i)
		arr[i] = int(input())
	return arr
		
numD = getNumDigits()
if numD > 0:
	list = [None] * numD
	list = getDigits(list)
	print('\nArray before sorting:')
	print('Number of digits in array: ', len(list))
	print('Digits in array:', str(list).replace(",", "").replace("[","").replace("]",""))
	print("\nArray after sorting: ")
	print('Number of digits in array: ', len(list))
	selectionSort(list)
	print('Digits in array:', str(list).replace(",", "").replace("[","").replace("]",""))
	
if numD == 0:	
	print('No digits to sort? Goodbye!')
