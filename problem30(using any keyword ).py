print("===================| LIST |===================")
# Lists
list = [1, 2, 3, 4]
a = any(list)
print("The result for list is : ", a)  # Output: True (at least one element is non-zero)

list2 = [0, False]
c = any(list2)
print("The result for list2 is : ", c)  # Output: False (all elements are zero or False)

list3 = [0, False, 5]
c = any(list3)
print("The result for list3 is : ", c)  # Output: True (5 is non-zero)

list1 = [1, 2, 3, 0, 4]
b = any(list1)
print("The result for list1 is : ", b)  # Output: True (at least one element is non-zero)

list3 = []
d = any(list3)
print("The result for list3 is : ", d)  # Output: False (empty list is considered false)

# Strings
print("===================| STRING |===================")
s = 'welcome to python'
print(any(s))  # Output: True (all characters are non-zero, even spaces)

s = '000'
print(any(s))  # Output: True (all characters are non-zero)

s = ' '
print(any(s))  # Output: True (space is considered non-zero)

# Dictionaries
print("===================| dictionaries |===================")
s = {0: 'False', 1: 'True'}
print(any(s))  # Output: True (1 is non-zero)

s = {1: 'False', 2: 'True'}
print(any(s))  # Output: True (all keys are non-zero)

s = {1: 'True', False: 0}
print(any(s))  # Output: True (1 is non-zero)

s = {}
print(any(s))  # Output: False (an empty dictionary is considered false)

s = {'0': 'True'}
print(any(s))  # Output: True (key '0' is a string, considered non-zero)
