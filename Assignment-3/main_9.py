def outer_function(a, b):
    
    def inner_function(x, y):
       
        return x + y

    addition = inner_function(a, b)
    
    result = addition + 5
    return result

a = 10
b = 20
print(f"The result is: {outer_function(a, b)}")