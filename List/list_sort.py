list_fruit=['orange', 'apple', 'pear', 'banana', 'kiwi']

list_fruit.sort()
print("Sorted list is :", list_fruit)

list_fruit.sort(reverse=True)
print("Sorted list in descending order :", list_fruit)

print(sorted(list_fruit,key=len))

list_fruit.sort(key=len)
print("Sorted list with key(len) in descending order :", list_fruit)
