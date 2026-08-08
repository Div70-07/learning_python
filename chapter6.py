"""***************CONDITIONAL STATEMENTS***************"""

a = 10
b = 9

if a > b:
    print("a is greater than b")  # This will be printed because the condition is True.             
elif a < b:
    print("a is less than b")  # This will not be printed because the condition is False.
else:
    print("a is equal to b")  # This will not be printed because the condition is False.

#Q1
print("Q1. Accept two numbers and print the greatest between them.")
x = int(input("Give value of x - "))
y = int(input("Give value of y - ")) 
if x>y:
    print(f"{x} is greater")
elif x<y:
    print(f"{y} is greater")
else:
    print("Both are equal")


#Q2
print("Q2. Accept gender from User and print greeting message.")
gender = input("Enter M for male & F for female")
if gender == "M":
    print("Good Morning Sir")
else: 
    print("Good Morning Ma'am")

#Q3
print("Q3. Accept and integer and check if its is even or odd")
num = int(input("Enter a number - "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#Q4
print("Q4. Accept name and age -- Check if the user is a valid voter(18+)")
age = int(input("Enter your age - "))
name = input("Enter your name - ")
if age>=18:
    print(f"Hey {name}, You are a valid voter.")
else:
    print(f"{name}, you are not a valid voter")

#5
print("Q5. Accept a year and tell if its a leap year.")
year = int(input("Enter a year: "))
if year%100==0 and year%400==0:
    print(f"{year} is a leap year")
elif year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Q6
print("Q6. Temperature ladder -- Accept temperature in degreee celsius and print a description (-5 == Freezing cold, 25== Pleasant, 45== Very Hot)")
temp=int(input("Enter temperatre in Celsius - "))
if temp<=-5:
    print("Freezing cold")
elif temp<=25:
    print("Pleasant")
else:
    print("Very Hot")
