# ZeroDivisionError

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print(f"The result is {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program finished.")

# NameError

try:
    print(my_variable)
    
except NameError:
    print("Error: Variable is not defined!")

print("Program finished.")

# EOFError

try:
    user_input = input("Enter something (press Ctrl+D or Ctrl+Z to simulate EOF): ")
    print(f"You entered: {user_input}")

except EOFError:
    print("Error: End of file (EOF) reached unexpectedly!")

print("Program finished.")

# ImportError

try:
    import non_existent_module
    
except ImportError:
    print("Error: Could not import the module or component!")

print("Program finished.")


# IndentationError

try:
    def greet(name):
    print(f"Hello, {name}!") 
    greet("Buddy") 

except IndentationError:
    print("Error: Indentation issue detected!")  

print("Program finished.")

# ValueError

try:
    user_input = input("Enter a number: ")
    number = int(user_input)  
    print(f"You entered the number: {number}")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

print("Program finished.")