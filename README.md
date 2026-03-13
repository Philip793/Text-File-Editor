#Python Text File Browser & Editor

A simple desktop application built with Python and Tkinter that allows users to browse, open, edit, and save text files from a directory through a graphical interface.
This project demonstrates fundamental Python development concepts including GUI programming, file handling, and exception management.

##Features

Browse .txt files located in the current directory
Open selected text files within a GUI editor
Edit file contents directly in the application
Save modifications back to the file
User-friendly error handling and feedback messages
Dynamic file loading using Python filesystem operations

##Technologies Used

###Python

###Tkinter (GUI framework)

###OS module for filesystem interaction

##How It Works

The application scans the current working directory for .txt files and displays them in a list.

###Users can:

Select a file from the list
Open the file in the editor
Modify the text
Save the updated contents back to the file
The program includes validation and error handling to ensure that files are properly selected before performing operations.

##Running the Application
Requirements

Python 3.x installed

##Steps

1. Clone the repository
``` bash
git clone https://github.com/Philip793/<repo-name>.git
```
2. Navigate to the project directory
``` bash
cd <repo-name>
```

3. Run the program
``` bash

python main.py
```
Example Workflow
1. Launch the application

2. Select a .txt file from the list

3. Click Open Selected

4. Edit the text in the editor

5. Click Save to overwrite the file

##Learning Outcomes

This project demonstrates:
Python GUI development using Tkinter
File input/output operations
Error handling and user feedback
Event-driven programming
Basic desktop application architecture

##Future Improvements

Possible enhancements include:
Ability to create new text files
Directory selection instead of using only the current folder
Syntax highlighting
Support for additional file types
Undo/redo functionality

