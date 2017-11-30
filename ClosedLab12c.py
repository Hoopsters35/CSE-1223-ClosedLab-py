def getFileName():
	name = input('Enter an input name: ')
	while not name:
		print('Error: Name can not be empty\n')
		name = input('Enter an input name: ')
	return name
def getOutFileName():
	name = input('Enter an output file name: ')
	while not name:
		print('Error: Name can not be empty\n')
		name = input('Enter an output file name: ')
	return name
try:
	fileName = getFileName()
	file = open(fileName, "r")
	#print(file.read()[::-1])
	outFileName = getOutFileName()
	outfile = open(outFileName, "w")
	outfile.write(file.read()[::-1])
except:
	print('Error')
finally:
	file.close()
	outfile.close()