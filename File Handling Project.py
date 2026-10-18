from pathlib import Path #Path is used to track the files running in the folder
import os  #imports os for delete functionality

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*')) 
    for i, items in enumerate(items):  #i is for numbering and items stores file names
        print(f"{i+1} : {items}")


def createfile():
    try:  #used try so that we can handle a exception if user enters a wrong file name
        readfileandfolder()
        name = input("Enter file name: ")
        p = Path(name) #creates a new file
        if not p.exists():

            with open(p,"w") as fs:  #opened file p in write mode
                data = input("Enter the data you want to include in file: ")
                fs.write(data)  #the given data is written in the file

            print("File created successfully")

        else:
            print("This file already exists")

    except Exception as err:
        print(f"an error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file(): 
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print("readed successfully")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error occurred as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content of your file")

            res = int(input("tell your response: "))

            if res == 1:
                name2 = input("Enter new name for the file: ")
                p2 = Path(name2)
                p.rename(p2)
                print("renamed successfully")

            if res == 2:
                with open(p, "w") as fs:
                    data = input("tell what you want to overwrite: ")
                    fs.write(data)
                print("Overwrite successfull")

            if res == 3:
                with open(p, "a") as fs:
                    data = input("Enter data to be appended: ")
                    fs.write(" "+data)
                print("Appended successfully")

        else:
            print("Wrong file name!")

    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            confirm = input(f"Delete '{p}'? (y/n): ").lower()
            if confirm == "y":
                os.remove(p)
                print("File removed successfully")
            else:
                print("Deletion Cancelled")
                
        else:
            print("there is no such file")

    except Exception as err:
        print(f"An error occured as {err}")


def main():
    while True:
        print("\n1. Create  2. Read  3. Update  4. Delete  5. Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            createfile()
        elif choice == "2":
            readfile()
        elif choice == "3":
            updatefile()
        elif choice == "4":
            deletefile()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


