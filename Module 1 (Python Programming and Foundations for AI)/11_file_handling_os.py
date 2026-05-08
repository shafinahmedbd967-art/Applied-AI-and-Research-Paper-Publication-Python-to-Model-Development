import os

# basic file write

# w mode creates the file if it doesnt exist, overwrites if it does
f = open("notes.txt", "w")
f.write("Python is great for AI\n")
f.write("This is line 2\n")
f.write("This is line 3\n")
f.close()   # always close after opening - but with is better (shown below)

print("File written successfully")
# Output: File written successfully


# basic file read

f = open("notes.txt", "r")
content = f.read()   # reads the entire file at once
f.close()

print(content)
# Output: Python is great for AI
# Output: This is line 2
# Output: This is line 3


# read just one line

f = open("notes.txt", "r")
first_line = f.readline()   # reads only one line
f.close()

print(first_line)
# Output: Python is great for AI


# read line by line

f = open("notes.txt", "r")
for line in f:
    print(line.strip())   # strip() removes the extra newline at the end
f.close()
# Output: Python is great for AI
# Output: This is line 2
# Output: This is line 3


# ----- why with is better -----

# without with - risky, if error happens close() never runs
# f = open("notes.txt", "r")
# data = f.read()
# f.close()   # might never reach here if error occurs above

# with with - file closes automatically even if error happens
with open("notes.txt", "r") as f:
    data = f.read()
    print(data)
# Output: Python is great for AI
# Output: This is line 2
# Output: This is line 3

# file is already closed here automatically


# reading line by line with with
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
# Output: Python is great for AI
# Output: This is line 2
# Output: This is line 3


# read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(lines)
# Output: ['Python is great for AI\n', 'This is line 2\n', 'This is line 3\n']

print(lines[0].strip())
# Output: Python is great for AI

print("Total lines:", len(lines))
# Output: Total lines: 3


# append mode - adds to existing content

with open("notes.txt", "a") as f:
    f.write("This line was added later\n")

with open("notes.txt", "r") as f:
    print(f.read())
# Output: Python is great for AI
# Output: This is line 2
# Output: This is line 3
# Output: This line was added later


# ----- write mode warning - it erases everything -----

with open("notes.txt", "w") as f:
    f.write("Fresh start - old content is gone\n")

with open("notes.txt", "r") as f:
    print(f.read())
# Output: Fresh start - old content is gone


# os module - for working with files and folders

# current working directory - where python is running from
cwd = os.getcwd()
print("Current directory:", cwd)
# Output: Current directory: D:\Applied AI and Research Paper Publication (Python to Model Development)


# path exists

print(os.path.exists("notes.txt"))
# Output: True

print(os.path.exists("fake_file.txt"))
# Output: False


# isfile and isdirectory

print(os.path.isfile("notes.txt"))
# Output: True

print(os.path.isdir("notes.txt"))
# Output: False

# checking a folder
print(os.path.isdir("."))    # . means current directory
# Output: True


# os.mkdir - make a new folder

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder created")
else:
    print("Folder already exists")
# Output: Folder created


# os.makedirs creates nested folders all at once
nested_path = os.path.join("test_folder", "subfolderA", "subfolderB")
os.makedirs(nested_path, exist_ok=True)   # exist_ok means no error if already exists
print("Nested folders created")
# Output: Nested folders created


# ----- os.path.join - building paths safely -----

# never manually write paths like "folder/subfolder/file.txt"
# because windows uses backslash and linux uses forward slash
# os.path.join handles this automatically

base = "Applied AI and Research Paper Publication (Python to Model Development)"
subfolder = "Module 1 (Python Programming and Foundations for AI)"
filename = "notes.txt"

full_path = os.path.join(base, subfolder, filename)
print(full_path)
# Output: Applied AI and Research Paper Publication (Python to Model Development)/Module 1 (Python Programming and Foundations for AI)/notes.txt


# list directory contents

contents = os.listdir(".")   # . means current folder
print(contents)
# Output: ['.git', 'Module 1 (Python Programming and Foundations for AI)', 'notes.txt', 'README.md', 'test_folder']


# check files in a folder - filtering out .idea and hidden folders 

def list_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist:", folder_path)
        return

    print("Contents of:", folder_path)
    for item in os.listdir(folder_path):

        # skip hidden folders like .idea, .git etc
        if item.startswith("."):
            continue

        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            print("  FILE:", item)
        elif os.path.isdir(item_path):
            print("  FOLDER:", item)

list_files_in_folder(".")
# Output: Contents of: .
# Output:   FILE: notes.txt
# Output:   FILE: 11_file_handling_os.py
# Output:   FOLDER: test_folder


# ----- check only python files in a folder -----

def list_python_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Not a valid directory:", folder_path)
        return []

    py_files = []
    for item in os.listdir(folder_path):
        if item.endswith(".py"):
            py_files.append(item)

    return py_files

py_files = list_python_files(".")
print("Python files found:", py_files)
# Output: Python files found: ['11_file_handling_os.py']


# ----- real world ml project folder structure setup -----

def create_ml_project_structure(project_name):
    folders = [
        project_name,
        os.path.join(project_name, "data"),
        os.path.join(project_name, "data", "raw"),
        os.path.join(project_name, "data", "processed"),
        os.path.join(project_name, "models"),
        os.path.join(project_name, "notebooks"),
        os.path.join(project_name, "outputs"),
        os.path.join(project_name, "logs"),
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print("Created:", folder)

    # create a starter readme
    readme_path = os.path.join(project_name, "README.txt")
    with open(readme_path, "w") as f:
        f.write("Project: " + project_name + "\n")
        f.write("Structure created automatically\n")

    print("Project structure ready")


create_ml_project_structure("my_ml_project")
# Output: Created: my_ml_project
# Output: Created: my_ml_project/data
# Output: Created: my_ml_project/data/raw
# Output: Created: my_ml_project/data/processed
# Output: Created: my_ml_project/models
# Output: Created: my_ml_project/notebooks
# Output: Created: my_ml_project/outputs
# Output: Created: my_ml_project/logs
# Output: Project structure ready


# -----actual course folder structure check -----

course_folder = "Applied AI and Research Paper Publication (Python to Model Development)"
module_folder = os.path.join(course_folder, "Module 1 (Python Programming and Foundations for AI)")

def inspect_folder(path):
    if not os.path.exists(path):
        print("Path does not exist:", path)
        return

    print("Inspecting:", path)
    print("Is a folder:", os.path.isdir(path))

    for item in os.listdir(path):
        if item.startswith("."):
            continue   # skip .idea and other hidden stuff

        item_full = os.path.join(path, item)

        if os.path.isfile(item_full):
            size = os.path.getsize(item_full)
            print("  FILE:", item, "| size:", size, "bytes")
        elif os.path.isdir(item_full):
            print("  FOLDER:", item)

inspect_folder(module_folder)
# Output will show the actual files and folders inside Module 1