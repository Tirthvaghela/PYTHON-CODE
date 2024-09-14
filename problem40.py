# Hierarchical Inheritance
class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Cat(Animal):
    def meow(self):
        print("Cat meows.")

dog = Dog()
cat = Cat()

dog.sound()   
dog.bark()    

cat.sound()   
cat.meow()    