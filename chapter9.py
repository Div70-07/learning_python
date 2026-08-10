"""*********************WHILE LOOP*******************"""

print("Seperate each digit of a number and print on a new line")
num = int(input("Enter a number: "))
while num>0:
    digit = num%10
    print(digit)
    num = num//10

print("Accept a number and print its reverse")
num=int(input("Enter a number: "))
rev=0
while num>0:
    rev = rev*10+(num%10)
    num = num//10
print(rev)


print("Check if a number is palindrome or not")
num=int(input("Enter a number: "))
org_num=num
rev=0
while num>0:
    rev = rev*10+(num%10)
    num = num//10
if org_num==rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
