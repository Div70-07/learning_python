"""******POLYMORPHISM******"""

def a():
    print("I am Ram")
def a():
    print("I am Overridden - Shyam") #Over-rides the previous one
a()


class Animal:
    def speak(self):
        print("Animal doesn't talk.")

class Humans:
    def speak(self):
        print("Humans do talk.")

obj1 = Animal()
obj2 = Humans()

obj1.speak()
obj2.speak()
#Both have same method names but are giving different responses, 
#This is Polymorphism, Single name -> Different forms.

"""Method Overriding"""
class child:
    def __init__(self, name):
        self.name = name
    def details(self):
        print(f"{self.name} is a child.")

class student(child):
    def __init__(self, name, id):
        self.id = id
        super().__init__(name)

    def details(self):
        super().details() #This line can be used to target the method of parent class
        print(f"{self.name} is a student with ID {self.id}.")

obj = student("Dev", 25)
obj.details() #This details calls student method's details as it is overridden.