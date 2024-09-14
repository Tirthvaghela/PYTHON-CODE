# Multiple Inheritance
class Father:
    def set_name(self):
        self.name = "Father"
    
    def show(self):
        print(f"{self.name} is working.")

class Mother:
    def set_hobby(self):
        self.hobby = "Gardening"
    
    def display(self):
        print(f"Mother's hobby is {self.hobby}.")

class Child(Father, Mother):
    def info(self):
        print("Child inherits from both Father and Mother.")

child1 = Child()

child1.set_name()   
child1.set_hobby()  

child1.show()       
child1.display()    
child1.info()       
