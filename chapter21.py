"""*************Constructor************"""
class Bags:
    def __init__(self, material, zips, pockets):
        self.material = material #Instance attribute -> Attribute created using an instance like self.name, self.age etc.
        self.zips = zips
        self.pockets = pockets

#Creating an object with a value
reebok = Bags("leather", 3, 2)
campus = Bags("polyster", 4,2)

print(reebok.material)
print(campus.material)
