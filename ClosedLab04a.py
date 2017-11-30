grade = float(input('Enter a grade value between 0 and 100: '))
while (grade < 0 or grade > 100):
	grade = float(input('ERROR: Grade must be between 0 and 100: '))
if (grade > 93):
	print('You received an A')
elif (grade > 90):
	print('You received an A-')
elif (grade > 87):
	print('You received a B+')
elif (grade > 83):
	print('You received a B')
elif (grade > 80):
	print('You received a B-')
elif (grade > 77):
	print('You received a C+')
elif (grade > 73):
	print('You received a C')
elif (grade > 70):
	print('You received a C-')
elif (grade > 67):
	print('You received a D+')
elif (grade > 60):
	print('You received a D')
else:
	print('You received an E')