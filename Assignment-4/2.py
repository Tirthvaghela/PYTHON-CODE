a= int(input("Enter Value of A :  "))

try :
    b= int(input("Enter Value of b :  "))
    if b==0 :
        raise ValueError

except ValueError:
    print(f"Second number is : {b}"," ,So exception")
else:
    print(f"Division : {a/b}")
