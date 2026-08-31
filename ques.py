print("Print a right-angle triangle with stars")
n = int(input("Enter number of lines: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print("")
print("")

print("Print a mirrored right-angle triangle.")

for i in range(1, n+1):
    for j in range(n-i, -1, -1):
        print(" ", end="")

    for j in range(1, i+1,1):
        print("*", end="")

    print("")

print("")


print("Print a centered diamond with stars.")

n=int(input("Enter the length of diamond:"))
for i in range(1, n+1):
    for j in range(n-i, -1, -1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print("")

for i in range(n, 0, -1):
    for j in range(0,n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*" , end="")
    print("")
print("")

