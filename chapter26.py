"""*******ABSTRACTION*********"""

from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass

#Inheriting the enforce class which is an abstract class forces the child class to 
#create the same method as abstract class or else throws an error.
class bike(enforce): 
    def enginestart():
        pass

class car(enforce):
    def enginestart():
        pass

class truck:
    pass

obj1 = bike()
obj2 = car()
obj3 = truck()