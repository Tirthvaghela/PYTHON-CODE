#Program to add natural.... sum = 1+2+3+...+n

n = int(input("Enter n: "))
sam = 0
i = 1

while i <= n:
    sam = sam + i
    i = i+1    
print("The sum is", sam)
