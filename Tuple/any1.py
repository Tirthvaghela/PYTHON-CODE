list1 = [1, 3, 4, 5]
print(any(list1))

list1 = [0, False]
print(any(list1))

list1 = [1, 3, 4, 0]
print(any(list1))

list1 = [0, False, 5]
print(any(list1))

list1 = []
print(any(list1))

print("any() for Strings")
s = "Welcome to Python"
print(any(s))

s = '000'
print(any(s))

s = ''
print(any(s))

print("any() for Dictionaries")
d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))