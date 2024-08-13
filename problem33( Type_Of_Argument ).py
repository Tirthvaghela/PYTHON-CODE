# 1. Required (Positional) Arguments
def add(a, b):
    "Adds two numbers."
    return a + b

# Call with required arguments
result = add(3, 5)
print("Sum (Required):", result)  # Output: Sum (Required): 8

# 2. Keyword Arguments
def multiply(a, b):
    "Multiplies two numbers."
    return a * b

# Call with keyword arguments (order doesn't matter)
result = multiply(b=4, a=3)
print("Product (Keyword):", result)  # Output: Product (Keyword): 12

# 3. Default Arguments
def power(base, exponent=2):
    "Raises a number to a power, with a default exponent of 2."
    return base ** exponent

# Call with and without the default argument
result1 = power(5)
result2 = power(5, 3)
print("Power with default exponent:", result1)  # Output: Power with default exponent: 25
print("Power with custom exponent:", result2)   # Output: Power with custom exponent: 125

# 4. Variable-length Arguments (*args and **kwargs)
def message(*val):
    sum = 0  
    for vall in val:
        sum += vall 
    print(sum)

# Calling the function
message(56, 3)  # Output: 59
message(4, 2)   # Output: 6
