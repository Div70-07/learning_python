"""DUNDER METHOD"""
#STARTS AND ENDS with double underscore, automatically gets called when we perform certain actions on an object.

class person:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Hello my name is {self.name}"

obj = person("Dev")
obj1 = person("Ram")
print(obj)
print(obj1)


class numbers:
     def __init__(self, num):
          self.num = num

     def __add__(self, other):
          return self.num + other.num

     def __eq__(self, value):
          return self.num == value.num

num1 = numbers(30)
num2 = numbers(30)

print(num1 + num2)
print(num1 == num2)