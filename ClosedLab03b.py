s1 = str(input('Enter the first string: '))
s2 = str(input('Enter the second string: '))
if s1 < s2:
	print(s1 + " comes before " + s2 + " lexiographically")
elif s2 < s1:
	print(s2 + " comes before " + s1 + " lexiographically")