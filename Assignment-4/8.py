class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa


print("=====|Student 1|=====")

name=input("Enter Name : ")
age=int(input("Enter Age : "))
major=input("Enter major : ")
gpa=float(input("Enter gpa : "))

print("\n=====|Student 2|=====")

n1=input("Enter Name : ")
age1=int(input("Enter Age : "))
major1=input("Enter major : ")
gpa1=float(input("Enter gpa : "))



student1 = Student(name,age, major, gpa)
student2 = Student(n1,age1, major1, gpa1)



print("=====|Student 1|=====")
print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Major: {student1.major}")
print(f"GPA: {student1.gpa}")

print("\n=====|Student 2|=====")
print(f"Name: {student2.name}")
print(f"Age: {student2.age}")
print(f"Major: {student2.major}")
print(f"GPA: {student2.gpa}")
