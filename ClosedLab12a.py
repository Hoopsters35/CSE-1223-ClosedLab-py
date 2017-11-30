def getFileName():
	name = input('Enter an input name: ')
	while not name:
		print('Error: Name can not be empty\n')
		name = input('Enter an input name: ')
	return name

fileName = getFileName()
file = open(fileName, "r")
for line in file:
	print(line[::-1])
