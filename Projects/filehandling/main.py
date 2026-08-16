from pathlib import Path


def createfile():
    try:
        name = input("Enter your file name: ")
        path = Path(name)

        if path.exists():
            choice = input("File already exists. Do you want to overwrite it? (y/n): ").strip().lower()
            if choice != "y":
                print("File creation cancelled.")
                return

        with open(path, "w") as fs:
            data = input("What do you want to write: ")
            fs.write(data)
        print("File created/updated successfully!!")
    except Exception as err:
        print(f"Error occurred as {err}")


def readfile():
    try:
        name = input("Enter the file name to read: ")
        path = Path(name)

        if not path.exists():
            print("File not found.")
            return

        with open(path, "r") as file:
            content = file.read()

        if not content:
            print("The file is empty.")
            return

        print("\nFile content:")
        choice = input("Press 1 to read the whole file, 2 to search for a word: ").strip()

        if choice == "2":
            keyword = input("Enter the word or phrase to search for: ")
            if keyword in content:
                print(f"The word '{keyword}' was found.")
                for line_number, line in enumerate(content.splitlines(), start=1):
                    if keyword in line:
                        print(f"Line {line_number}: {line}")
            else:
                print("Keyword not found.")
        else:
            print(content)
    except Exception as err:
        print(f"Error occurred as {err}")


def updatefile():
    try:
        name = input("Enter the file name to update: ")
        path = Path(name)

        if not path.exists():
            print("File not found.")
            return

        print("Choose an update option:")
        print("1. Overwrite the file")
        print("2. Append content")
        print("3. Rename the file")
        option = input("Enter your choice: ").strip()

        if option == "1":
            new_data = input("Enter new content to write: ")
            with open(path, "w") as file:
                file.write(new_data)
            print("File overwritten successfully!!")

        elif option == "2":
            new_data = input("Enter content to append: ")
            with open(path, "a") as file:
                file.write(new_data)
            print("Content appended successfully!!")

        elif option == "3":
            new_name = input("Enter the new file name: ").strip()
            if not new_name:
                print("Rename cancelled.")
                return

            new_path = Path(new_name)
            if new_path.exists():
                print("New file name already exists. Choose a different one.")
                return

            path.rename(new_path)
            print(f"File renamed successfully to {new_path}")

        else:
            print("Invalid update option.")
    except Exception as err:
        print(f"Error occurred as {err}")


def deletefile():
    try:
        name = input("Enter the file name to delete: ")
        path = Path(name)

        if path.exists():
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm == "y":
                path.unlink()
                print("File deleted successfully!!")
            else:
                print("Delete operation cancelled.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred as {err}")

