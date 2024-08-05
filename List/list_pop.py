list_lang = ['Python', 'Java', 'C++', 'French', 'C']

return_value = list_lang.pop(3)
print('Return Value: ', return_value)
print('Updated List: ', list_lang)

print('Return Value: ', list_lang.pop(-3))
print('Updated List: ', list_lang)

print('Return Value: ', list_lang.pop())
print('Updated List: ', list_lang)

print('Return Value: ', list_lang.pop(-1))
print('Updated List: ', list_lang)