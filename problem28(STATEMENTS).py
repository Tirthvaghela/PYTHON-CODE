# BREAK STATEMENT
print('====BREAK====')
for letter in 'Python':
    if letter == 'h':
        break  # STOP WHEN 'h' COMES
    print("Letter:", letter)

# CONTINUE STATEMENT
print('====CONTINUE====')
for letter in 'Python':
    if letter == 'h':
        continue  # SKIP 'h'
    print("Letter:", letter)

# PASS STATEMENT
print('====PASS====')
for letter in 'Python':
    if letter == 'h':
        pass  # NOTHING TO DO, JUST PASS
    print("Letter:", letter)
