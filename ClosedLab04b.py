inp = input('Enter a time in HH:MM AM/PM format: ')
hour = int(inp[:inp.index(':')])
minute = int(inp[inp.index(':') + 1:inp.index(':') + 3])
t = inp[len(inp) - 2: len(inp)]
milT = 0


if t.upper() == 'AM':
	if not hour == 12:
		milT = hour * 100 + minute
	else: milT = minute
elif t.upper() == 'PM':
	if not hour == 12:
		milT = hour * 100 + 1200 + minute
	else: milT = 1200 + minute
	

print('Time in military time is: ' + str(milT))