"""ENCAPSULAION"""

class factory:
    name = "Kia" #public class
    _old = 12 #Protected using "_" ->Single underscore
    __country="Japan" #Private using "__" -> Double underscore

    def __init__(self,type,tyre,color):
        self.color = color #Public_object_attribute
        self.__tyre = tyre #Private_object_attribute
        self.type = type

    def detail(self): #Public_Method
        print(f"Hello your details are: {self.color} {self.type} {self.__tyre}")

class company(factory):
    print(factory.name)
    print(factory._old)
    #print(factory.__country) -> This will throw an error as it can't be accessed

obj = factory("Sedan","MRF","Black")

print(obj.name) #Can be accessed as its public
#print(obj.__country) -> Can't be accessed as its private

obj.color = "Blue" #Color changes to blue as its public
obj.__tyre = "Cheat" #No change takes place cause its private

obj.detail()


class hello:
    __a=12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = hello()

#obj.__a() will cause error
obj.info() #This will call __a from classmethod
