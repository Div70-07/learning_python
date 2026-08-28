"""*****************INHERITANCE***************"""

class Animal: #Parent class
    a = 10
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Hello my name is {self.name}")

class Humans(Animal): #Child Class
    pass

obj = Animal("Lion")
obj2 = Humans("Dev")

obj.details()
obj2.details()
print(obj2.a)

#Child class objects an access all the attributes and methods 
#of parent class.

"""Constructor in Inheritance"""

class BagFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your bag details are: ")
        print(self.material)
        print(self.zips)
        print(self.pockets)

class reebok(BagFactory): #Single_Level_Inheritance
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets)
        self.color = color

    def details(self):
        print(self.color)
        return super().details()

class campus(reebok): #Multi_Level_Inheritance
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets, color)
    

bag1 = BagFactory("Leather", 1, 2)
bag2 = reebok("Polyster", 4, 2, "Matte Black")

bag1.details()
bag2.details()


#Multiple Inheritance

class a:
    def __init__(self, name):
        self.name = name

class b:
    def __init__(self, id):
        self.id = id

class c(a,b):
    def __init__(self, name, id):
        a.__init__(self, name)
        b.__init__(self, id)

    def details(self):
        print("Student details are: ")
        print(self.name)
        print(self.id)

student = c("Dev", 25)
student.details()