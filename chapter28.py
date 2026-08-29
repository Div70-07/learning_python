"""ADVANCED TOPICS"""

"""DECORATORS"""

#Whenever we call any function and it has decorator on top then 
#we can print that function start and end with any statement

def extragreeting(func):
    def wrapper():
        print("Hello dear, ")
        func() #Here, the function will get called.
        print("How are you?")
    return wrapper


@extragreeting 
def greetings():
    print("Good Morning")

greetings()


"""args & kwargs"""

#*args -> In any function using "*" can start accepting any number of 
# arguements/ variables as input and stores them in Tuple.

def addition(*args):
    s=0
    for i in args:
        s=s+i
    return s

print (addition(20,30,10,50,90))


#kwargs - Keyword argument -> Stores any number of data in dictionary


def info(**kwargs):
    return kwargs

print(info(name = "Akarsh", age=24, profession="SDE"))


def msg(calc):
    def wrapper(*args):
        print("Here's your answer: ")
        calc(*args)
        print("Thank you for using me.")
    return wrapper

@msg
def add(a,b,c):
    print(a+b+c)

@msg
def multiply(a,b,c,d):
    print(a*b*c*d)

add(10,20,30)
multiply(2,3,4,5)
 
#Ternary operation
a=20
print("Even number") if a%2==0 else print("Odd number")


"""*******Comprehensions*******"""

#List Comprehension

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[i for i in a if i%2==0]

print(b)

# Dict comprehension
squared = {a: a**2 for a in range(5)}   # {0:0,1:1,2:4...}

# Set comprehension
unique = {x%3 for x in range(10)}       # {0,1,2}

"""LAMBDA FUNCTIONS"""

check = lambda x: "even number" if x%2==0 else "odd number"
print(check(12))

addition = lambda a,b : a+b
print(addition(10,20))


"""map(), filter(), zip()"""

nums = [1, 2, 3, 4, 5]

# map — transform every item
doubled = list(map(lambda x: x*2, nums))  # [2,4,6,8,10]

# filter — keep items that pass the test
evens = list(filter(lambda x: x%2==0, nums)) # [2,4]

# zip — combine two lists into pairs
names  = ["A", "B", "C"]
scores = [90, 85, 78]
pairs  = list(zip(names, scores))  # [('A',90),('B',85),...]


"""Modules & Packages"""

# Built-in modules
import math
import random
from datetime import datetime

print(math.sqrt(16))           # 4.0
print(random.randint(1, 100))  # random number
print(datetime.now())           # current date/time

# Third-party (install with pip)
# pip install numpy pandas matplotlib