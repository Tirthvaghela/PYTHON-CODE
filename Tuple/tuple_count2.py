random1 = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

count = random1.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)

count = random1.count([3, 4])
print("The count of [3, 4] is:", count)