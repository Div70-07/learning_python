"""Tuple - A tuple is a collection which is ordered and unchangeable.
 Allows duplicate members. Use tuples for data that should stay constant 
 — like days of the week, coordinates, or config values."""

mytuple = ("apple", "banana", 123, 567)
print(mytuple)
print(type(mytuple))


#List to Tuple - Storing list as Tuple using Tuple function
a = ["monday", "Tuesday", 1178]
tup = tuple(a)
print(tup)
print(type(tup))
 
#tup[0] = "Sunday" --> TypeError: 'tuple' object does not support item assignment
#Immutable Nature

#Python itself assigns any function and any defined variable into a tuple.
def student():
    return "Ram", 24, "Ram@gmail.com"
info = student()
print(info)
print(type(info))
a=12,13,14,15,16
print(a)
print(type(a))