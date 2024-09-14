# Multi-Level Inheritance
class Grandfather:
    def display_grandfather(self):
        print("Grandfather's wisdom is valuable.")

class Father(Grandfather):
    def display_father(self):
        print("Father works hard.")

class Son(Father):
    def display_son(self):
        print("Son is learning.")

son1 = Son()

son1.display_grandfather()  
son1.display_father()       
son1.display_son()          
