# Constructors
class Employee:
    def __init__(self, name, salary):
        self.name = input("Enter Name : ")  
        self.salary = int(input("Enter Salary : ")) 

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

employee1 = Employee("", 0)

employee1.show_details()
