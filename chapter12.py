"""***************DATA STRUCTURES***************"""


"""1. list - A list is a collection which is ordered and changeable. Allows duplicate members."""
basket = ["apple", "banana", "cherry"]  
print(type(basket))

a = [10,11,17,23,80]
print(a[2]) #Ordered nature - Can access the elements using index.
#print(a[0:3]) #Can access the elements using slicing.
print(a[-1]) #Can access the elements using negative indexing.
a[-1] = 100 #Changeable nature - Can change the value of an element using indexing.
print(a[-1])
a[1]=10 #It can store duplicate values as well.
print(a)


a.append(9)        # [10,10,17,23,80,9]   — add to end
print(a)
a.insert(0, 0)     # [0,10,10,17,23,80,9] — insert at index
print(a)
a.remove(10)       # removes first 10
print(a)
a.sort()           # sort ascending
print(a)
a.reverse()        # reverse in place
print(a)
len(a)             # number of items
print(len(a))
print("")

#Traversing a list
a = [10,11,17,23,80]
for i in a: #Traversing on values
    print(i)
for i in range(0, len(a)): #Traversing on indices
    print(f"Index {i}: {a[i]}")
print("*******QUESTIONS**********")
print("Q1. Print all positive and negative elements seperately.")
list = [3, -1, 4, -5, 9]
pos =[]
neg = []
for i in list:
    if i<0:
        pos.append(i)
    else:
        neg.append(i)
print(f"Positive elements = {pos}, Negative elements={neg}")
print("")

print("Q2. Find the mean(Average) of all elements in list.")
l=[10, 20, 30 ,40, 100]
sum = 0
for i in l:
    sum += i;
avg = sum/(len(l));
print(f"Average = {avg}")
print("")

print("Q3. Find the greatest element and print its index.")
l = [102,4,70,80,100,90,101]
m = l.sort()
print(f"Greatest element is {l[len(l)-1]} and its index is {len(l)-1} using sort function")

l = [102,4,70,80,100,90,101]
greatest =l[0];
for i in range(len(l)):
    if(l[i]>greatest):
        greatest = l[i]
print(f"Greatest element = {greatest}, Index = {l.index(greatest)}")
print("")


print("Q4. Find the second largest number.")
l = [12,4,70,80,100,900,101,150,200,800]
largest = l[0]
slargest = l[0]
for i in l:
    if i > largest:
        slargest=largest
        largest=i
    elif i > slargest  and i != largest:
        slargest = i
print(largest)
print(slargest)
print("")


print("Q5. Check if the list is sorted")
l = [10, 20, 30, 30, 40, 50]
count = 0
for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        count += 1
if count == 0:
    print("List is Sorted.")
else:
    print("List is not sorted")
print("")















"""
#2. set - A set is a collection which is unordered and unindexed. No duplicate members.
myset = {"apple", "banana", "cherry"}  
print(type(myset))


#3. tuple - A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#4. dict - A dictionary is a collection which is ordered, changeable and indexed. No duplicate members.
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}  
print(type(mydict))
print(mydict)

"""