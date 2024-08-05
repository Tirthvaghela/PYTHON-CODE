#tuple and list inside a list
veg = ['banana', 'orange', ('apple', 'lime'), ['mango', 'strawberry'], ['mango', 'strawberry'], 'orange']

print(type(veg))
index = veg.index(('apple', 'lime'))
print("The index of ('apple', 'lime'):", index)

index = veg.index(['mango', 'strawberry'])
print("The index of ['mango', 'strawberry']:", index)

count=veg.count(['mango', 'strawberry'])
print("Count of  ['mango', 'strawberry'] is : ", count)

count1=veg.count('orange')
print("Count of orange is : ", count1)

count2=veg.count('banana')
print("Count of banana is : ", count2)