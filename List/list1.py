My_list = ['Shoes', 'Bottle', 'Purse', 'Belt']

print('I have', len(My_list), 'items to purchase.')

print('These items are:')
for item in My_list:
    print(item)

print('\nI also have to buy earphone.')
My_list.append('earphone')
print('My shopping list is now',My_list)

print('I will sort my list now')
My_list.sort()
My_list.sort()

print('Sorted shopping list is', My_list)

print('The first item I will buy is', My_list[0])
olditem = My_list[0]
del My_list[0]
print('I bought the', olditem)
print('My shopping list is now', My_list)
