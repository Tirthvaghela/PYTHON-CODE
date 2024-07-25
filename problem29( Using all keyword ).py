print("===================| LIST |===================")
# Lists
list = [1, 2, 3, 4]
a = all(list) 
print("The result for list is : ", a)  # Output: True (all elements are non-zero)

list1 = [1, 2, 3, 0, 4]
b = all(list1)  
print("The result for list1 is : ", b)  # Output: False (0 is considered false)

list2 = [0, False]
c = all(list2) 
print("The result for list2 is : ", c)  # Output: False (both elements are false)

list3 = []
d = all(list3)  
print("The result for list3 is : ", d)  # Output: True (an empty list is considered true)

# Strings
print("===================| STRING |===================")
s = 'welcome to python'
print(all(s))  # Output: True (all characters are non-zero, even space)

s = '000'
print(all(s))  # Output: True (all characters are non-zero)

s = ' '
print(all(s))  # Output: True (space is considered non-zero)

# Dictionaries
print("===================| dictionaries |===================")
s = {0: 'False', 1: 'True'}
print(all(s))  # Output: False (0 is considered false)

s = {1: 'False', 2: 'True'}
print(all(s))  # Output: True (all keys are non-zero)

s = {1: 'True', False: 0}
print(all(s))  # Output: False (False is considered zero)

s = {}
print(all(s))  # Output: True (an empty dictionary is considered true)

s = {'0': 'True'}
print(all(s))  # Output: True (key '0' is a string, considered non-zero)
