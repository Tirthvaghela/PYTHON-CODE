print("===================| LIST |===================")
# Lists
list=[1,2,3,4]
a=all(list)  # Checks if all elements in the list are truthy (non-zero, non-empty, True)
print("The result for list is : ", a)

list1=[1,2,3,0,4]
b=all(list1)  # Checks if all elements in the list are truthy
print("The result for list1 is : ", b)

list2=[0,False]
c=all(list2)  # Checks if all elements in the list are truthy
print("The result for list2 is : ", c)

list3=[]
d=all(list3)  # Checks if all elements in the empty list are truthy (always True for empty lists)
print("The result for list3 is : ", d)

# Strings
print("===================| STRING |===================")
s='welcome to python'
print(all(s))  # Checks if all characters in the string are truthy (non-empty)

s='000'
print(all(s))  # Checks if all characters in the string are truthy

s=' '
print(all(s))  # Checks if all characters in the string are truthy

# Dictionaries
print("===================| dictionaries |===================")
s={0:'False', 1:'True'}
print(all(s))  # Checks if all keys in the dictionary are truthy (non-zero, non-empty)

s={1:'False', 2:'True'}
print(all(s))  # Checks if all keys in the dictionary are truthy

s={1:'True', False:0}
print(all(s))  # Checks if all keys in the dictionary are truthy

s={}
print(all(s))  # Checks if all keys in the empty dictionary are truthy (always True for empty dictionaries)

s={'0':'True'}
print(all(s)) 