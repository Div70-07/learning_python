"""*******************Input, Output & Operators******************"""

name="Dev"
age=24

print("Hey!")
print(f"My name is {name} and my age is {age}") 
#Using f makes it a formatted string
print("My name is {name} and my age is {age}") 
#Without using f name and age won't be taken into account and simply be printed as they are in code
print("My name is",name,"and my age is",age)
#Another simple way of writing with values

age = int(input("What is your age:-")) 
#We are converting any kind of input to integer using int() function. 
#Input is always taken as string by default. So it needs to be converted into desired data type.
print(f"Hey! It's nice to meet someone aged {age}")


""""***************************Operators*******************************"""
#Arithmetic Operators - int, float, complex
#(+,-,*,/,//,%,**)

a = 20
b = 3
print(a+b) #Addition
print(a+b+b+20) #Addition with multiple variables
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division -> Its a fraction form so it will return float result.
print(a//b) #Floor Division -> It will return the integer part of the division result.
print(a%b) #Modulus -> It will return the remainder of the division.
print(a**b) #Exponentiation -> It will return the result of raising a to the power of b.

#Arithmetic operators follows BODMAS rule. 
"""
()-> Brackets/ Parentheses
** -> Exponentiation
*, /, //, % -> Multiplication, Division, Floor Division, Modulus
+, - -> Addition, Subtraction
"""
print(10/2*5) #25.0
print(10*2/5) #4.0
# Python follow left to right rule for operators of same precedence. 
# So in the above example, 10/2 is calculated first and then multiplied by 5. In the second example, 10*2 is calculated first and then divided by 5.

#Comparison Operators 
#(==, !=, >, <, >=, <=)
print(5 == 5)  # True
print(5 != 5)  # False
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 5)  # True
print(5 <= 3)  # False

#Logical Operators
#(and, or, not)
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

#Assignment Operators
#(=, +=, -=, *=, /=, //=, %=, **=)
x = 5
x += 3  # x = x + 3
print(x)  # 8
x -= 2  # x = x - 2
print(x)  # 6
x *= 4  # x = x * 4
print(x)  # 24
x /= 3  # x = x / 3
print(x)  # 8.0