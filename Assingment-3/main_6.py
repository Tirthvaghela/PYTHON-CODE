def calculation(x, y):
    addition = x + y
    subtraction = x - y
    return addition, subtraction

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

result = calculation(num1, num2)
print(f"Addition: {result[0]}")
print(f"Subtraction: {result[1]}")