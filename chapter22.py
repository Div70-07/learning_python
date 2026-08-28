"""TYPES OF Methods & Attributes"""

class Animal:
    a = 12 #1. Class attribute

    def __init__(self, name):
        self.name = name #2. Object/instance attribute

    def hello(self): #1. Instance/object Method -> Captures the location of Object
        print(f"Hello, my name is {self.name}")

    @classmethod
    def details(cls): #2. Class method -> Captures the location of class
        print(f"How are you? I am {cls.a}")

    @staticmethod
    def speak(): #3. Static method -> Doesn't target any location
        print("Hey I am a static method")

obj = Animal("Lion")
obj.hello()
obj.details()
obj.speak()