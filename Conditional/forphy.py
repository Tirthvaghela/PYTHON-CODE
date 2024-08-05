# #usr/bin/python

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# for val in numbers:
# 	sum = sum+val
# print("The sum is", sum)




# Python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
	print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1,num + 1):
		factorial = factorial*i
	print("The factorial of",num,"is",factorial)

	
