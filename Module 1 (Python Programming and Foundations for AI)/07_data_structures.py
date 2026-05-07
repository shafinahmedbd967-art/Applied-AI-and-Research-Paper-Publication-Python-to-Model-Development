#  SECTION 1: LIST
# List is ordered, mutable (changeable), allows duplicate values
# Defined with square brackets []

students = ["Ayman", "Rafi", "Nila", "Sara", "Karim"]
scores   = [85, 92, 78, 95, 60, 88, 73]

# Basic Indexing 
print(students[0])                  # Ayman   (first element)
print(students[2])                  # Nila    (third element)
print(students[-1])                 # Karim   (last element)
print(students[-2])                 # Sara    (second from last)

#  Negative Indexing 
# Negative index counts from the END of the list
# -1 is last, -2 is second last, and so on
print(scores[-1])                   # 73
print(scores[-3])                   # 60

# Slicing: list[start:stop:step]─
# start  → inclusive (default 0)
# stop   → exclusive (default end)
# step   → jump size (default 1)

print(scores[0:3])                  # [85, 92, 78]   index 0,1,2
print(scores[2:5])                  # [78, 95, 60]   index 2,3,4
print(scores[:3])                   # [85, 92, 78]   from start
print(scores[3:])                   # [95, 60, 88, 73] to end
print(scores[::2])                  # [85, 78, 60, 73] every 2nd
print(scores[::-1])                 # [73, 88, 60, 95, 78, 92, 85] reversed

# Slicing with negative index
print(scores[-3:])                  # [88, 73, 60] last 3 — wait
print(scores[-3:])                  # [60, 88, 73] last 3 elements

# List Methods 
students.append("Hasan")            # add to end
print(students)
# ["Ayman", "Rafi", "Nila", "Sara", "Karim", "Hasan"]

students.insert(1, "Zara")          # insert at index 1
print(students[1])                  # Zara

students.remove("Zara")             # remove by value
print(students)
# ["Ayman", "Rafi", "Nila", "Sara", "Karim", "Hasan"]

popped = students.pop()             # remove and return last element
print(popped)                       # Hasan

students.sort()                     # sort alphabetically in place
print(students)                     # ['Ayman', 'Karim', 'Nila', 'Rafi', 'Sara']

print(len(students))                # 5
print("Ayman" in students)          # True
print(students.index("Nila"))       # 2


#  SECTION 2: TUPLE
# Tuple is ordered, IMMUTABLE (cannot be changed), allows duplicates
# Defined with parentheses ()
# Use tuple when data should NOT change — coordinates, RGB, config values

student_record = ("Ayman", 23, 3.85, "CSE")

print(student_record[0])            # Ayman
print(student_record[-1])           # CSE
print(student_record[1:3])          # (23, 3.85)

# Tuple unpacking — very common in Python
name, age, gpa, dept = student_record
print(name)                         # Ayman
print(gpa)                          # 3.85

# Tuple is immutable — this will raise TypeError
# student_record[0] = "Rafi"        # TypeError: 'tuple' object does not support item assignment

# Single element tuple needs a trailing comma
single = ("Ayman",)                 # this is a tuple
not_tuple = ("Ayman")               # this is just a string
print(type(single))                 # <class 'tuple'>
print(type(not_tuple))              # <class 'str'>

# Tuple as function return (already covered — returning multiple values)
def get_min_max(data):
    return min(data), max(data)     # returns a tuple

low, high = get_min_max([70, 85, 92, 60])
print(low, high)                    # 60 92


#   SECTION 3: LIST vs TUPLE — Difference and When to Use
# LIST  → mutable, use when data changes (adding students, updating scores)
# TUPLE → immutable, use when data is fixed (coordinates, RGB, DB records)

# Use LIST when:
enrolled_students = ["Ayman", "Rafi"]   # students can join/leave
enrolled_students.append("Nila")        # modification needed

# Use TUPLE when:
gps_coordinate  = (23.8103, 90.4125)    # Dhaka — should never change
rgb_red         = (255, 0, 0)           # color value — fixed
model_input_shape = (224, 224, 3)       # image shape in CNN — fixed

# Tuple is faster than List — Python optimizes immutable objects
import timeit
list_time  = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
print(f"List : {list_time:.4f}s")       # List : ~0.05s
print(f"Tuple: {tuple_time:.4f}s")      # Tuple: ~0.02s  (faster)

# Tuple can be used as dictionary KEY — list cannot (list is unhashable)
location_data = {
    (23.8103, 90.4125): "Dhaka",
    (51.5074, -0.1278): "London"
}
print(location_data[(23.8103, 90.4125)])    # Dhaka

 

#  SECTION 4: DICTIONARY
# Dictionary is key-value pairs, ordered (Python 3.7+), mutable
# Keys must be unique and immutable (str, int, tuple)
# Defined with curly braces {}

student = {
    "name"      : "Ayman",
    "age"       : 23,
    "gpa"       : 3.85,
    "enrolled"  : True
}

# Accessing values
print(student["name"])              # Ayman
print(student.get("age"))          # 23
print(student.get("email", "N/A")) # N/A  (default if key missing)

# Adding and updating
student["email"] = "ayman@ai.com"  # add new key
student["gpa"]   = 3.90            # update existing key
print(student["gpa"])              # 3.90

# Removing
del student["enrolled"]
popped = student.pop("email")
print(popped)                       # ayman@ai.com

# Iterating
for key in student:
    print(key, ":", student[key])
# name : Ayman
# age  : 23
# gpa  : 3.90

for key, value in student.items():
    print(f"{key} → {value}")
# name → Ayman
# age  → 23
# gpa  → 3.90

print(list(student.keys()))        # ['name', 'age', 'gpa']
print(list(student.values()))      # ['Ayman', 23, 3.90]

# Nested Dictionary
# Dictionary inside a dictionary — very common for structured data
# In ML: model configs, dataset metadata, API responses (JSON)

course_data = {
    "Applied AI": {
        "instructor"  : "Dr. Rahman",
        "total_seats" : 30,
        "students"    : {
            "Ayman": {"age": 23, "gpa": 3.85},
            "Rafi" : {"age": 25, "gpa": 3.50}
        }
    },
    "Deep Learning": {
        "instructor"  : "Dr. Khan",
        "total_seats" : 20,
        "students"    : {
            "Nila": {"age": 22, "gpa": 3.90}
        }
    }
}

# Accessing nested values
print(course_data["Applied AI"]["instructor"])
# Dr. Rahman

print(course_data["Applied AI"]["students"]["Ayman"]["gpa"])
# 3.85

# Iterating nested dictionary
for course, details in course_data.items():
    print(f"\nCourse: {course}")
    print(f"  Instructor: {details['instructor']}")
    for student, info in details["students"].items():
        print(f"  {student} — GPA: {info['gpa']}")

# Course: Applied AI
#   Instructor: Dr. Rahman
#   Ayman — GPA: 3.85
#   Rafi  — GPA: 3.50
#
# Course: Deep Learning
#   Instructor: Dr. Khan
#   Nila  — GPA: 3.90

 

#  SECTION 5: SET
# Set is unordered, mutable, NO duplicates allowed
# Defined with curly braces {} — but no key-value pairs
# Use when you need unique values or set operations

registered   = {"Ayman", "Rafi", "Nila", "Ayman", "Rafi"}
print(registered)                   # {'Nila', 'Rafi', 'Ayman'} — duplicates removed

# Adding and removing
registered.add("Sara")
registered.discard("Nila")          # discard does NOT raise error if missing
print(registered)                   # {'Rafi', 'Ayman', 'Sara'}

# Membership check — O(1) time, much faster than list
print("Ayman" in registered)        # True
print("Nila" in registered)         # False

# ── Set Operations ───────────────────────────────────────────────
batch_A = {"Ayman", "Rafi", "Nila"}
batch_B = {"Nila", "Sara", "Karim"}

print(batch_A | batch_B)            # Union — all students
# {'Ayman', 'Rafi', 'Nila', 'Sara', 'Karim'}

print(batch_A & batch_B)            # Intersection — common students
# {'Nila'}

print(batch_A - batch_B)            # Difference — only in batch_A
# {'Ayman', 'Rafi'}

print(batch_A ^ batch_B)            # Symmetric difference — not in both
# {'Ayman', 'Rafi', 'Sara', 'Karim'}

# Real use case — finding duplicate entries in dataset
raw_data   = [101, 102, 103, 101, 104, 102, 105]
unique_ids = list(set(raw_data))    # remove duplicates
print(unique_ids)                   # [101, 102, 103, 104, 105]

duplicates = [x for x in raw_data if raw_data.count(x) > 1]
print(set(duplicates))              # {101, 102}



# SECTION 6: LIST COMPREHENSION
# Syntax: [expression for item in iterable if condition]
# Creates a new list in a single readable line
# Faster than regular for loop + append

scores = [85, 92, 78, 95, 60, 45, 88]

# Filter passed scores (>= 70)
passed = [s for s in scores if s >= 70]
print(passed)                       # [85, 92, 78, 95, 88]

# Normalize scores to 0-1
max_score  = max(scores)
normalized = [round(s / max_score, 2) for s in scores]
print(normalized)                   # [0.89, 0.97, 0.82, 1.0, 0.63, 0.47, 0.93]

# Apply grade label using ternary inside comprehension
grades = ["Pass" if s >= 70 else "Fail" for s in scores]
print(grades)                       # ['Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass']

# Nested list comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [num for row in matrix for num in row]
print(flat)                         # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension with enumerate
students = ["Ayman", "Rafi", "Nila"]
indexed  = [f"{i+1}. {name}" for i, name in enumerate(students)]
print(indexed)                      # ['1. Ayman', '2. Rafi', '3. Nila']




#  SECTION 7: LIST COMPREHENSION IN DICTIONARY
#  (Building a list of dictionaries)

# building structured dataset records
names  = ["Ayman", "Rafi", "Nila"]
scores = [85, 92, 78]

# Build a list of student dictionaries
student_records = [
    {"name": name, "score": score, "grade": "Pass" if score >= 70 else "Fail"}
    for name, score in zip(names, scores)
]

for record in student_records:
    print(record)
# {'name': 'Ayman', 'score': 85, 'grade': 'Pass'}
# {'name': 'Rafi',  'score': 92, 'grade': 'Pass'}
# {'name': 'Nila',  'score': 78, 'grade': 'Pass'}


#  SECTION 8: DICTIONARY COMPREHENSION
# Syntax: {key: value for item in iterable if condition}
# Builds a dictionary in one line

names  = ["Ayman", "Rafi", "Nila", "Sara"]
scores = [85, 92, 78, 60]

# Map name → score
score_map = {name: score for name, score in zip(names, scores)}
print(score_map)
# {'Ayman': 85, 'Rafi': 92, 'Nila': 78, 'Sara': 60}

# Filter — only passing students
passed_map = {name: score for name, score in zip(names, scores) if score >= 70}
print(passed_map)
# {'Ayman': 85, 'Rafi': 92, 'Nila': 78}

# Transform values — normalize scores
max_score    = max(scores)
norm_map = {name: round(score / max_score, 2) for name, score in zip(names, scores)}
print(norm_map)
# {'Ayman': 0.92, 'Rafi': 1.0, 'Nila': 0.85, 'Sara': 0.65}

# Swap keys and values
inverted = {score: name for name, score in score_map.items()}
print(inverted)
# {85: 'Ayman', 92: 'Rafi', 78: 'Nila', 60: 'Sara'}


#  SECTION 9: CLASS-BASED INDEX ENUMERATION
# Using a class to represent indexed student data
# This is where OOP meets data structures

class StudentIndex:
    def __init__(self, students, scores):
        # Store as list of tuples — ordered, immutable records
        self.records = list(enumerate(zip(students, scores), start=1))

    def display(self):
        for index, (name, score) in self.records:
            grade = "Pass" if score >= 70 else "Fail"
            print(f"[{index}] {name:10} | Score: {score} | {grade}")

    def get_by_index(self, index):
        # index is 1-based here
        for idx, (name, score) in self.records:
            if idx == index:
                return {"index": idx, "name": name, "score": score}
        return None

    def to_dict(self):
        # Convert to dictionary comprehension
        return {name: score for _, (name, score) in self.records}


students = ["Ayman", "Rafi", "Nila", "Sara"]
scores   = [85, 92, 78, 60]

si = StudentIndex(students, scores)
si.display()
# [1] Ayman      | Score: 85 | Pass
# [2] Rafi       | Score: 92 | Pass
# [3] Nila       | Score: 78 | Pass
# [4] Sara       | Score: 60 | Fail

print(si.get_by_index(2))
# {'index': 2, 'name': 'Rafi', 'score': 92}

print(si.to_dict())
# {'Ayman': 85, 'Rafi': 92, 'Nila': 78, 'Sara': 60}