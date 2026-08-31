"""
Python Dictionary

A dictionary is a collection of key-value pairs.
- It stores data in pairs like: key : value
- Keys must be unique.
- Values can be repeated.
- A dictionary is ordered in Python 3.7+.
- It is changeable (you can update values).
- It is useful for storing data that is connected to a name or label.

Example:
student = {"name": "Aisha", "age": 21, "course": "Python"}

This means:
- key = "name"
- value = "Aisha"

Vanilla Python:
Vanilla Python means plain Python without using any extra libraries or frameworks.
So if we use only built-in Python features like lists, sets, dictionaries, loops, and functions,
we are working in vanilla Python.

Example:
student = {"name": "Aisha", "age": 21}
print(student["name"])

This is basic Python, no pandas, no numpy, no Django, no Flask.
"""

# 1) Creating a dictionary
# A dictionary is created with curly braces { }
student = {"name": "Aisha", "age": 21, "course": "Python"}
print("Student details:", student)
print("Type:", type(student))

# 2) Accessing values
# We access values using the key inside square brackets []
print("Name:", student["name"])
print("Age:", student["age"])

# 3) Adding a new key-value pair
student["city"] = "Lahore"
print("After adding city:", student)

# 4) Updating an existing value
student["age"] = 22
print("After updating age:", student)

# 5) Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# 6) Dictionary with different value types
person = {
    "name": "Ali",
    "age": 25,
    "is_student": True,
    "skills": ["Python", "ML", "Data Science"]
}
print("Person info:", person)

# 7) Example of nested dictionary
# A dictionary can contain another dictionary
student_profile = {
    "name": "Zara",
    "marks": {"math": 90, "science": 85, "english": 88}
}
print("Student profile:", student_profile)
print("Math marks:", student_profile["marks"]["math"])

# Methods
# Most commonly used dictionary methods

# get(key, default): returns the value if key exists, otherwise default value
print("Using get():", student.get("name", "Not found"))
print("Using get() on missing key:", student.get("phone", "No phone number"))

# keys(): returns all keys in the dictionary
print("Keys:", student.keys())

# values(): returns all values in the dictionary
print("Values:", student.values())

# items(): returns key-value pairs as tuples
print("Items:", student.items())

# pop(key): removes a key and returns its value
removed_value = student.pop("city")
print("Removed city:", removed_value)
print("After pop:", student)

# update(): adds or updates multiple key-value pairs
audio = {"name": "speaker", "price": 2000}
audio.update({"brand": "Sony", "stock": 10})
print("After update:", audio)

# clear(): removes all items from the dictionary
student.clear()
print("After clear():", student)

# 8) Checking if a key exists
if "name" in student:
    print("'name' exists in the dictionary")
else:
    print("Name dosen't exists")

# 9) Why dictionaries are useful
# They are very useful for storing real-world data like:
# student information, product details, database rows, and JSON data.

# Example: product data
product = {
    "product_id": 101,
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000
}
print("Product:", product)

#Traversing
d={10:100,20:200,30:300,40:400}
for i in d:
    print(i)
    print(d[i])
    print(f"key {i} : Value {d[i]}")

# Summary:
# Dictionary = key-value data structure
# Keys are used to access values quickly
# They are important in Python, AI, and ML because data is often stored as dictionaries
# like JSON, config files, model metadata, and dataset labels.

print("Q1. Merge two dictionaries into one.")
d1={"a":1,"c":3,"e":5}
d2={"b":2,"d":4,"f":6}
#d1.update(d2)
for i in d2:
    d1[i]=d2[i]
print(d1)    


print("Q2.Sum all values in dictionary")
sum = 0
for i in d1:
    sum = sum + d1[i]
print(f"Total sum = {sum}")

print("Q3. Count the frequency of each element in a list using a dictionary.")
list = ["a", "a", "b", "c", "c", "d", "b", "b"]
dic = {}
for i in list:
    if i in dic.keys():
        dic[i] = dic[i]+1
    else:
        dic[i]=1
print(dic)

print("Q4. Combine two dicts, adding values for common keys.")
d1={"a":1,"b":3,"d":5}
d2={"b":2,"d":4,"e":6}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)