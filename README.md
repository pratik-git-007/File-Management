# Python File Manager

A simple command-line tool built in Python for managing files from the terminal. It lets you create, read, update, and delete files through an interactive menu.

## Features

- Create a new file with custom content
- Read and display the contents of any file
- Rename a file, overwrite its content, or append to it
- Delete files with a confirmation prompt
- Lists the files and folders before each operation
- Menu loop that keeps running until you choose Exit

## Tech Used

- Python 3
- `pathlib` for path handling
- `os` for file deletion

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Run the project

```bash
git clone https://github.com/<your-username>/File-Management.git
cd File-Management
python file_manager.py
```

## Usage

When you run the script, you will see this menu:

```
1. Create  2. Read  3. Update  4. Delete  5. Exit
Your choice:
```

| Option | What it does |
|--------|--------------|
| 1 | Create a new file and write content into it |
| 2 | Read the content of an existing file |
| 3 | Rename, overwrite, or append to a file |
| 4 | Delete a file (asks for confirmation first) |
| 5 | Exit the program |

### Example

```
1. Create  2. Read  3. Update  4. Delete  5. Exit
Your choice: 1
1 : file_manager.py
Enter file name: notes.txt
Enter the data you want to include in file: Hello, world!
File created successfully
```

## What I Learned

- File handling in Python (read, write, append)
- Working with `pathlib`
- Basic exception handling
- Building a menu-driven CLI program

## Future Improvements

- Create and delete folders
- Better input validation in the update menu
- Prevent renaming over an existing file
- Logging of operations

## Author

Pratik
