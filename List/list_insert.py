bank_list=['sbi','hdfc','kotak']
bank_tuple=('rbi','mahindra')

print('Original bank list:', bank_list)

bank_list.insert(2,'icici')
print('Updated bank list:', bank_list)

bank_list.insert(1,bank_tuple)
print('Original bank list:', bank_list)
