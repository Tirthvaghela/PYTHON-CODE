n1=int(input("Enter a non-negative number : "))
try:
	if n1<0:
		raise Exception
except Exception:
	print("You choose Negative : ",n1)
else:
	print("You choose positive: ",n1)
