def getList():
	list = []
	temp = input("Enter a word ('XXX' to quit): ")
	while not temp.lower() == 'xxx':
		list.append(temp)
		temp = input("Enter a word ('XXX' to quit): ")
	return list
	
def printList(title, list):
	print(title)
	print('-' * len(title))
	counter = 0
	for i in list:
		print(str(counter) + ": " + str(i))
		counter += 1
	print()
	
def appendLists(l1, l2):
	out = []
	for i in l1:
		out.append(i)
	for o in l2:
		out.append(o)
	return out
	
def mergeLists(l1, l2):
	out = []
	minL = 0
	counter = 0
	if len(l1) < len(l2):
		minL = len(l1)
	else: minL = len(l2)
	while counter < minL:
		out.append(l1[counter])
		out.append(l2[counter])
		counter += 1
	while counter < len(l1):
		out.append(l1[counter])
		counter += 1
	while counter < len(l2):
		out.append(l2[counter])
		counter += 1
	return out
		
print('Enter the first wordlist:')
l1 = getList()
print('Enter the second wordlist:')
l2 = getList()
printList('Wordlist 1', l1)
printList('Wordlist 2', l2)
l12 = appendLists(l1, l2)
printList('List 2 appended to the end of List 1', l12)
l21 = appendLists(l2, l1)
printList('List 1 appended to the end of List 2', l21)
l3 = mergeLists(l1, l2)
printList('List 1 merged with List 2', l3)
l4 = mergeLists(l2, l1)
printList('List 2 merged with List 1', l4)