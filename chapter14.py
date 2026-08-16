"""
Sets

A set is an unordered collection of unique items.
- It does not keep duplicate values.
- It is not indexed like a list.
- It has no guaranteed order.
- It is useful for membership checks and set math operations.

Important idea:
Python stores set values using their hash values.
A hash is a number generated from the item.
This helps Python quickly find, insert, and check values in a set.
"""

# 1) Creating a set
# A set is created using curly braces { }
# Duplicates are automatically removed.
fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits set:", fruits)
print("Type:", type(fruits))

# 2) Sets are unordered
# A set does not remember the insertion order.
# So the output may appear in a different order each time.
numbers = {10, 20, 30, 40}
print("Numbers set:")
for item in numbers:
    print(item)

# 3) Checking membership in a set
# This is very fast because Python uses hashing internally.
print("banana" in fruits)
print("grape" in fruits)

# 4) Removing duplicates from a list
# Converting a list into a set keeps only unique values.
nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7]
unique_nums = set(nums)
print("Original list:", nums)
print("Unique numbers:", unique_nums)

# 5) Set operations
# These are like math operations on sets.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)      # values in either set
print("Intersection:", A & B)  # common values
print("Difference:", A - B)    # values in A not in B
print("Symmetric difference:", A ^ B)  # values in one set only

# 6) Hash function in Python
# Python uses the hash() function to get an integer hash value.
# Hash values are used to organize items in a set.
name = "hello"
print("Hash of 'hello':", hash(name))

# How set storage works internally:
# 1. Python computes the hash of each item.
# 2. It uses that hash to decide where the item should be stored.
# 3. This makes membership tests very fast.
# 4. If two items have the same hash, Python resolves that collision.
# 5. The set then compares the items to make sure they are truly equal.

# Example with a number and a string
print("Hash of 42:", hash(42))
print("Hash of '42':", hash("42"))

# Why sets require hashable items
# Strings, numbers, and tuples are hashable, so they can go in sets.
# Lists and dictionaries are not hashable, so they cannot be used directly in a set.
# Example:
# my_list = [1, 2, 3]
# {my_list}  # This would raise TypeError because lists are unhashable.

# 7) Adding and removing items
my_set = {"a", "b", "c"}
my_set.add("d")
print("After add:", my_set)

my_set.remove("b")
print("After remove:", my_set)

# 8) Most useful set methods
# These are the methods developers use most often when working with sets.

# add(x): Adds a single item to the set.
letters = {"a", "b"}
letters.add("c")
print("add():", letters)

# clear(): Removes all items from the set.
letters.clear()
print("clear():", letters)

# copy(): Returns a shallow copy of the set.
nums = {1, 2, 3}
nums_copy = nums.copy()
print("copy():", nums_copy)

# union(*others): Returns a new set with all items from both sets.
A = {1, 2, 3}
B = {3, 4, 5}
print("union():", A.union(B))

# intersection(*others): Returns items common to all sets.
print("intersection():", A.intersection(B))

# difference(*others): Returns items in this set that are not in others.
print("difference():", A.difference(B))

# symmetric_difference(other): Returns items in either set, but not both.
print("symmetric_difference():", A.symmetric_difference(B))

# discard(x): Removes x if present; does nothing if not present.
skills = {"python", "sql", "ml"}
skills.discard("sql")
print("discard():", skills)

# remove(x): Removes x; raises KeyError if x is not found.
# skills.remove("java")  # This would raise an error.

# pop(): Removes and returns a random item from the set.
random_item = skills.pop()
print("pop():", random_item, "Remaining:", skills)

# update(*others): Adds all items from other iterables into the set.
set1 = {1, 2}
set1.update([2, 3, 4])
print("update():", set1)

# issubset(other): Checks if all items of this set are in another set.
print("issubset():", {1, 2}.issubset({1, 2, 3}))

# issuperset(other): Checks if this set contains all items of another set.
print("issuperset():", {1, 2, 3}.issuperset({1, 2}))

# isdisjoint(other): Checks if two sets have no common elements.
print("isdisjoint():", {1, 2}.isdisjoint({3, 4}))

# Summary:
# Sets are amazing for unique values, fast checks, and set math.
# Python uses hashing to store and retrieve items efficiently.
# In AI/ML, sets are often used to remove duplicates from labels, features, and token lists.

