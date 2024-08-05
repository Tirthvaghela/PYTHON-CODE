sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
sales2 = {'carrot':5}
print(sales.keys())
print(sales.values())
print(sales.items())
sales.update(sales2)
print("After update",sales)
#print(sales.has_key('apple'))
#print(sales.has_key('potato'))
print(sales.get('orange'))
print(sales.get('brinjal'))