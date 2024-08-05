num=(1,2,3,4,5,6,7,8,9,10,11)
c_odd=0
c_even=0
for x in num:
	if x%2==0:
		c_even+=1
	else:
		c_odd+=1
print("Numbers of even numbers ", c_even)
print("Numbers of odd numbers ", c_odd)
