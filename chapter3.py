#DATATYPE

"""In python there are different types of data types. Some of them are:"""
#1. int (Varies from negative infinity to positive infinity)
x = 5 #only 5 has a dataype, and that is bieng captured by the variable x.
print(type(x))  

#2. float
y = 5.5 
z = 12/3 #if there is p/q form then it will be float data type.
print(type(y))
print(type(z))

#3. complex - Real + Imaginary
w = 3 + 4j
print(type(w))

#4. bool - True or False
a = True    
print(type(a))

#5. str - String : We can store not only text but numbers, special characters, and spaces in string data type.  
b = "Hello" 
str = 'Dev said, "He has started learning python."'
print(type(b))
print(str)
print(type(str))

#6. None - None is a data type of its own (NoneType) and only None can be None.
c = None    
print(type(c))

#7. set - A set is a collection which is unordered and unindexed. No duplicate members.
myset = {"apple", "banana", "cherry"}  
print(type(myset))

#8. list - A list is a collection which is ordered and changeable. Allows duplicate members.
mylist = ["apple", "banana", "cherry"]  
print(type(mylist))

#9. tuple - A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#10. dict - A dictionary is a collection which is ordered, changeable and indexed. No duplicate members.
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}  
print(type(mydict))
print(mydict)

