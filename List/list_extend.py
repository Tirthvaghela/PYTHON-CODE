vegetable = ['potato', 'tomato', 'brinjal']
fruit = ['mango', 'apple']
vegetable_tuple=('carrot', 'beans')

vegetable.extend(fruit)
print('Extended vegetable/fruit list: ', vegetable) 

vegetable.extend(vegetable_tuple)
print('Extended vegetable tuple list: ', vegetable) 

vegetable.sort()
print(vegetable)