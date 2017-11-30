for i in range(1, 11):
	
	for j in range(1, 11):
		if i * j < 10:
			print(i * j, end = "   ")
		elif i* j < 100:
			print(i * j, end = "  ")
		elif i * j < 1000:
			print(i * j, end = " ")
	print()