'''Write a Python program which will have Main Menu for performing following operations
based on selection:
Main Menu:
Airthmetic Operation
Identity Operator Operation
Logical Operation
Member Operator Operation'''

print("Main Menu:")
print("1. Arithmetic Operation")
print("2. Identity Operator Operation")
print("3. Logical Operation")
print("4. Member Operator Operation")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("You selected Arithmetic Operation")
elif choice == 2:
    print("You selected Identity Operator Operation")
elif choice == 3:
    print("You selected Logical Operation")
elif choice == 4:
    print("You selected Member Operator Operation")
else:
    print("Invalid choice")
