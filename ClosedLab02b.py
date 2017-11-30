from math import sqrt
l1 = float(input("Enter the length of the first side: "))
l2 = float(input("Enter the length of the second side: "))
print("The perimeter of your rectangle is " + str(2 * l1 + 2 * l2))
print("The area of your rectangle is " + str(l1 * l2))
print("The length of the diagonal is " + str(sqrt(l1**2 + l2**2)))
print("Goodbye!")
