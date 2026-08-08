"""**************Strings & Type Conversion***************"""

x ="a"
print(ord(x)) #ord() function returns the Unicode code point for a one-character string.
print(chr(65)) #chr() function returns the string for a Unicode code point.

"""**************String indexing****************"""

#Positive indexing
y="Hello"
print(y[0]) #H
print(y[1]) #e
print(y[2]) #l
print(y[3]) #l
print(y[4]) #o
#Negative indexing
print(y[-1]) #o
print(y[-2]) #l
print(y[-3]) #l
print(y[-4]) #e
print(y[-5]) #H

#String slicing
z="Hello World"
print(z[1:5:1])  #z[start:stop:step] -> ello
print(z[6:10:1])  #z[start:stop:step] -> Worl
print(z[0:11:2])  #z[start:stop:step] -> HloWrd
print(z[::2])  #z[start:stop:step] -> HloWrd Default values for start, stop and step are 0, len(string) and 1 respectively.
print(z[0:11:3])  #z[start:stop:step] -> Hl r

a = "Hello How are you?"
print(a[6:9:1]) #how
print(a[14:17:1]) #you
print(a[0:6:1]) #Hello


"""***********TYPE CONVERSION**************"""
b="12"
c= int(b)
print(b)
print(c)
print(type(b))#STRING
print(type(c))#INTEGER

d=12.4
e=int(d)
print(e)
print(type(e))#INTEGER

f=str(d)
print(f)
print(type(f))#STRING - Anything can be converted to string

#Boolean conversion -->
"""Only 7 values convert to FALSE rest all coverts to TRUE.
1. False
2. 0
3. 0.0
4. "Empty_String"
5. [Empty Tuple]
6. (Empty List)
7. {Empty Dictionary}"""
