try:
    n = int(input("Enter a number: "))
    print(f"Your age is : {n}")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")