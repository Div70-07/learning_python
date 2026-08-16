from pathlib import Path


def createfile():
    try:
        name = input("Enter your file name: ")
        path = Path(name)
        
        if not path.exists():
            with open (path,"w") as fs:
                data = input("What you want to write: ")
                fs.write(data)
            print("File Created Successfully!!")
        else:
            print("File name already exists")
    except Exception as err:
        print(f"Error occured as {err}")         

def readfile():
    try:
        name = input("Enter the file name to read: ")
        path = Path(name)

        if path.exists():
            with open(path, "r") as file:
                content = file.read()

            if content:
                print("\nFile content:")
                print(content)
            else:
                print("The file is empty.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred as {err}")


def updatefile():
    try:
        name = input("Enter the file name to update: ")
        path = Path(name)

        if path.exists():
            new_data = input("Enter new content to write: ")
            with open(path, "w") as file:
                file.write(new_data)
            print("File updated successfully!!")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred as {err}")


def deletefile():
    try:
        name = input("Enter the file name to delete: ")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("File deleted successfully!!")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred as {err}")


print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deleting a file")

a = int(input("\nTell your response: "))
if a == 1:
    createfile()
elif a == 2:
    readfile()
elif a == 3:
    updatefile()
elif a == 4:
    deletefile()
else:
    print("Invalid choice.")
