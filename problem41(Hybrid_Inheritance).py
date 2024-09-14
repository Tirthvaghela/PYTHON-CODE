# Hybrid Inheritance
class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Cat(Animal):
    def meow(self):
        print("Cat meows.")

class Pet(Dog, Cat):
    def play(self):
        print("Pets love to play.")

my_pet = Pet()

my_pet.sound()   
my_pet.bark()    
my_pet.meow()    
my_pet.play()    
