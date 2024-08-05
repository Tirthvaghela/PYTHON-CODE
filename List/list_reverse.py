list_os = ['Windows', 'macOS', 'Linux','Ubuntu','Unix']
print('Original List:', list_os)

#Syntax: reversed_list = os[start:stop:step] 
reversed_list = list_os[::-1]
print('Updated List:', reversed_list)

reversed_list.reverse()
print('Updated List:', reversed_list)

for o in reversed(reversed_list):
	print(o)
