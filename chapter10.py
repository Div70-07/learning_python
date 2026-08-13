"""***********************FUNCTIONS***********************"""

def greet_user():   #def = define
    print("Hello!")

greet_user()
greet_user()  

#calling the function as many as times we want to use it.
#Reusable block of code is called function.
#It can be used multiple times in a program.

"""**********FUNCTIONS WITH PARAMETERS & ARGUMENTS**************"""

def addition(a,b):
    print(a+b) #a & b are parameters of the function addition.

addition(5, 3) #5 and 3 are arguments of the function addition.
addition(10, 20)
addition(100, 200)


def palindrome_checker(a):
    temp = a;
    rev = 0;
    while a>0:
        rev = rev*10+a%10
        a = a//10
    if temp == rev:
        print(f"{temp} is a palindrome")
    else:
        print(f"{temp} is not palindrome")

palindrome_checker(121)
palindrome_checker(90)

"""TYPES OF ARGUEMENTS"""

#1. Positional - order matters

def multiply(a,b,c,d):
    print(a*b*c*d)
#multiply(2,5,6) --> This throws an positional error as position d value is missing,
#the values are assigned based on the position they are in.

#2. Default - works even without passing a value

def addition(a,b,c=12): #after declaring a default value we can't declare a non-default value after it.
    print(a+b+c)

addition(5, 3) #c takes the default value of 12
addition(5, 3, 10) #c takes the value of 10

#3. Keyword — pass in any order

def subtraction(a,b,c):
    print(a-b-c)
subtraction(a=10,b=5,c=3) # Passing arguments as keywords
subtraction(c=3,a=10,b=5) # Order doesn't matter when using keyword arguments
subtraction(10,b=2,c=0) #Positional arguements can't be used after keyword arguments. 
#Once keyword arguments are used, all subsequent arguments must also be keyword arguments.