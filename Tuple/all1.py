list1 = [1, 3, 4, 5]
print(all(list1))

# all values false
list1 = [0, False]
print(all(list1))

# one false value
list1 = [1, 3, 4, 0]
print(all(list1))

# one true value
list1 = [0, False, 5]
print(all(list1))

# empty iterable
list1 = []
print(all(list1))

print("all() for Strings")
s = "Welcome to Python"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))

print("all() for Dictionaries")
s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))