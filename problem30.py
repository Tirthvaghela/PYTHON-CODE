# Tuple Function

print("===================| LIST |===================")
# Lists
list=[1,2,3,4]
a=any(list)  # Checks if any elements in the list are truthy (non-zero, non-empty, True)
print("The result for list is : ", a)

list2=[0,False]
c=any(list2)  # Checks if any elements in the list are truthy
print("The result for list2 is : ", c)

list3=[0,False,5]
c=any(list3)  # Checks if any elements in the list are truthy
print("The result for list3 is : ", c)

list1=[1,2,3,0,4]
b=any(list1)  # Checks if any elements in the list are truthy
print("The result for list1 is : ", b)


list3=[]
d=any(list3)  # Checks if any elements in the empty list are truthy (always True for empty lists)
print("The result for list3 is : ", d)

# Strings
print("===================| STRING |===================")
s='welcome to python'
print(any(s))  # Checks if any characters in the string are truthy (non-empty)

s='000'
print(any(s))  # Checks if any characters in the string are truthy

s=' '
print(any(s))  # Checks if any characters in the string are truthy

# Dictionaries
print("===================| dictionaries |===================")
s={0:'False', 1:'True'}
print(any(s))  # Checks if any keys in the dictionary are truthy (non-zero, non-empty)

s={1:'False', 2:'True'}
print(any(s))  # Checks if any keys in the dictionary are truthy

s={1:'True', False:0}
print(any(s))  # Checks if any keys in the dictionary are truthy

s={}
print(any(s))  # Checks if any keys in the empty dictionary are truthy (always True for empty dictionaries)

s={'0':'True'}
print(any(s)) 