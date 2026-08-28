"""********Objects**********"""
class bags:
    name="Factory name - ARP"

    def details(self):
        print("This company creates bags")

#Creating an object
reebok = bags() #Initialise a class into variable reebok ->> Object
campus = bags() #Single class can have multiple objects

#Accessing the attributes
print(reebok.name)
reebok.details() 