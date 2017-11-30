numDig = 0
nums = "0123456789"
inp = input('Enter a string to count the digits in: ')
for i in inp:
	if i in nums:
		numDig+=1
		
print("Your string contains " + str(numDig) + " digits.")
