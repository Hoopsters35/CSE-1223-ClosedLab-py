num = int(input('Enter a starting value: '))

while not num == 1:
	print(str(num), end = ", ")
	if num % 2 == 0:
		num //= 2
	elif num % 2 == 1:
		num = num * 3 + 1
print(str(num))
	
	