n1=int(input("Enter a number other than 3 : "))
try:
	if n1==3:
		raise Exception
except Exception:
	print("You choose in Exception : 3")
else:
	print("You choose : ",n1)
finally:
	print("Code Done")