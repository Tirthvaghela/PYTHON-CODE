while True :
    try:
        value = int(input("Please enter an integer value: "))
        break  
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"You have entered a valid integer: {value}")