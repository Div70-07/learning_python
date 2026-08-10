"""******************FOR LOOP******************"""

"""
range(start, stop, step) #Range goes from start to stop-1, with one step increments (+1)
range(start, stop) #Range goes from start to stop-1, with default step of (+1)
range(stop) #Range goes from 0 to stop-1, with default step of (+1)
"""

range(1, 11, 1) #1,2,3,4,5,6,7,8,9,10
range(23, 46) #23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45
range(21) #0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

for i in range(1, 11, 1):
    print(i) #Prints 1,2,3,4,5,6,7,8,9,10

for i in range(23, 46):
    print(i) #Prints 23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45

for i in range(21):
    print(i) #Prints 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20


#Table of 5 
for i in range(5,51,5):
    print(i)


#Table of any number n
"""num = int(input("Enter a number:- "))
for i in range(num, (num*10)+1, num):
    print(i)"""


#Loop for strings
a ="Python"
for i in a:
    print(i) #Prints P,y,t,h,o,n

for i in range(0,8):
    print(a) #Prints Python 8 times

for i in range(len(a)): #Iterates through the length of the string a
    print(a[i]) #Prints P,y,t,h,o,n



#Break, Continue & Else
for i in range(0,11):
    if i==4 or i==5:
        continue
    print(i)

for j in range(11,21):
    if j==19:
        break
    print(j)
else:
    print("No Break was encountered")

print("Q1. Print Hello World n times.")
a = "Hello WOrld"
n = int(input("Enter number of times: "))
for i in range (n):
    print(a)

print("Q2. Print natural numbers from 1 to n")
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)

print("Q3. Reverse for loop - print n down to 1.")
for i in range(n,0,-1):
    print(i)

print("Q4. Print sum of first n natural numbers")
num = int(input("Enter a natural number : "))
sum = 0
for i in range(1, num+1, 1):
    sum = sum + i
print (sum)

print("Q5. Factorial of a number")
num = int(input("Enter a number : "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)

print("Q6. Print sum of all even and odd numbers in a range seperately")
num = int(input("Enter a number: "))
Even_sum=0
Odd_sum=0
for i in range(1,num+1):
    if(i%2==0):
        Even_sum+=i
    else:
        Odd_sum+=i
print(f"Even sum ={Even_sum}")
print(f"Odd sum = {Odd_sum}")

print("Q7. Print all fators of a number")
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i)

print("Q8. Check if a number is perfect (sum of factors = the number itself).")
n = int(input("Enter a number: "))
factors_sum = 0
for i in range(1, n):
    if n % i == 0:
        factors_sum += i
if factors_sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")  

print("Q9. Check if a number is prime")
n = int(input("Enter a number: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")    


print("Q10. Reverse a String without using built in fucntions")
str = input("Enter a string: ")
reversed_str = ""
for i in range(len(str)-1, -1, -1):
    reversed_str += str[i]
print(f"Reversed string: {reversed_str}")

print("Q11. Check if a string is a palindrome.")
str = input("Enter a string: ")
reversed_str = ""
for i in range(len(str)-1, -1, -1):
    reversed_str += str[i]
print(f"Reversed string: {reversed_str}")
if reversed_str == str:
    print(f"'{str}' is a palindrome.")
else:
    print(f"'{str}' is not a palindrome.")

print("Q12. Count letters, digits, and special symbols in a string.")
str = input("Enter a string: ")
letters = 0
digits = 0
special_symbols = 0
for c in str:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    else:
        special_symbols += 1
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special symbols: {special_symbols}")