# Single Inheritance
class Animal:
    def set_name(self):
        self.name = input("Enter Animal Name (Eg : Dog): ")
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

dog1 = Dog()
dog1.set_name()  
dog1.speak()     
