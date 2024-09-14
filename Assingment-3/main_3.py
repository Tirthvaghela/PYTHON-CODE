from calculator import add, sub, mul, div

a = 10
b = 5

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")

try:
    print(f"{a} / 0 = {div(a, 0)}")
except ValueError as e:
    print(e)
