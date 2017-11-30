def larger(num1, num2):
	if num1 > num2:
		print(str(num1) + " is larger than " + str(num2))
	elif num2 > num1:
		print(str(num2) + " is larger than " + str(num1))
	else: print("The two numbers are equal")

n1 = float(input('Enter your first number: '))
n2 = float(input('Enter your second number: '))
larger(n1, n2)