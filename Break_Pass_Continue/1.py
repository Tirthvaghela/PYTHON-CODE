def display_even_index_characters():
   
    user_input = input("Enter a string: ")

    even_index_characters = ""

    for index in range(0, len(user_input), 2):
        even_index_characters += user_input[index]

    print("Characters at even index numbers:", even_index_characters)

display_even_index_characters()
