"""
File Handling in Python

File handling means working with files stored on the computer.
We can create files, write data into them, read data from them, and update them.

Why is file handling important?
- Save data permanently
- Read saved data later
- Store user input
- Work with text files, logs, and configuration files
- Use files in AI/ML projects for datasets, notes, and results

In Python, we use the open() function to work with files.
"""

# 1) Creating a new file with "x" mode
# "x" creates a file, but it will raise an error if the file already exists.
# Example:
# file = open("hello.txt", "x")

# 2) Writing to a file with "w" mode
# "w" means write. It creates the file if it does not exist.
# It overwrites the file if it already exists.
file_write = open("write.txt", "w")
data = input("What do you want to write in the file? ")
file_write.write(data)
file_write.close()

# 3) Reading a file with "r" mode
# "r" means read. This mode is used to read the file content.
file_read = open("write.txt", "r")
print("File content:")
print(file_read.read())
file_read.close()

# 4) Appending to a file with "a" mode
# "a" means append. It adds new text at the end of the file.
with open("write.txt", "a") as file_append:
    file_append.write(" " + "I want to see if it is working or not.")

# 5) Reading after appending
with open("write.txt", "r") as file_after_append:
    print("\nUpdated file content:")
    print(file_after_append.read())

# 6) Common file modes
# "r" -> read only
# "w" -> write only (overwrites file)
# "a" -> append (adds data at the end)
# "x" -> create a file only if it does not exist
# "r+" -> read and write
# "t" -> text mode (default)
# "b" -> binary mode

# 7) Writing multiple lines
with open("notes.txt", "w") as file_notes:
    file_notes.write("First line\n")
    file_notes.write("Second line\n")
    file_notes.write("Third line\n")

# 8) Reading line by line
with open("notes.txt", "r") as file_lines:
    print("\nReading lines one by one:")
    for line in file_lines:
        print(line.strip())

# 9) Reading a single line
with open("notes.txt", "r") as file_single_line:
    first_line = file_single_line.readline()
    print("\nFirst line:", first_line.strip())

# 10) Important methods
# read(): reads the whole file
# write(): writes data to the file
# readline(): reads one line
# readlines(): reads all lines into a list
# close(): closes the file after use
# flush(): forces data to be written immediately
# seek(): moves to a specific position in the file

# 11) Example of readlines()
with open("notes.txt", "r") as file_list:
    lines = file_list.readlines()
    print("\nList of lines:", lines)

# 12) Example of with open()
# with open() automatically closes the file after the block ends.
# This is safer and recommended in Python.
with open("example.txt", "w") as demo_file:
    demo_file.write("This file was created using with open().")

with open("example.txt", "r") as demo_file:
    print("\nExample file content:", demo_file.read())

# 13) File handling in real life
# Example: storing user details
user_name = "Hamza"
user_age = 20

with open("user_data.txt", "w") as user_file:
    user_file.write(f"Name: {user_name}\n")
    user_file.write(f"Age: {user_age}\n")

with open("user_data.txt", "r") as user_file:
    print("\nUser data:")
    print(user_file.read())

# 14) Best practices
# - Always close the file or use with open()
# - Use the right file mode
# - Handle errors using try/except
# - Do not overwrite data accidentally unless you want to

# Summary:
# File handling lets us create, read, write, and update files.
# The most important file modes are r, w, a, and x.
# with open() is the safest and easiest method to use.
# This is a basic skill used in Python projects, automation, and data work.

