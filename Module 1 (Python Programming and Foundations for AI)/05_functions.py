# ════════════════════════════════════════════════════════════════
# SECTION 1: Basic Function — No Parameter, No Return
# ════════════════════════════════════════════════════════════════

# A simple function that just prints a message
# No input, no output — just executes a block of code
def greet():
    print("Welcome to Applied AI Course!")

greet()                                     # Welcome to Applied AI Course!
greet()                                     # Welcome to Applied AI Course!
# Same function called twice — no code repetition


# ════════════════════════════════════════════════════════════════
# SECTION 2: Function with Parameters
# ════════════════════════════════════════════════════════════════

# Parameters are variables that receive values when the function is called
# 'name' and 'age' are parameters here
def greet_student(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_student("Ayman", 23)                  # Hello Ayman, you are 23 years old.
greet_student("Rafi", 25)                   # Hello Rafi, you are 25 years old.


# ════════════════════════════════════════════════════════════════
# SECTION 3: Function with Return Value
# ════════════════════════════════════════════════════════════════

# 'return' sends a value back to the caller
# Without return, function returns None by default
def calculate_age_difference(age1, age2):
    difference = abs(age1 - age2)           # abs() gives absolute value
    return difference

result = calculate_age_difference(23, 25)
print(result)                               # 2

# Return value can be used directly in expressions
print(calculate_age_difference(30, 18) > 5) # True


# ════════════════════════════════════════════════════════════════
# SECTION 4: Default Arguments
# ════════════════════════════════════════════════════════════════

# Default arguments are used when no value is passed for that parameter
# Must always be defined AFTER non-default parameters
def enroll_student(name, course="Applied AI", fee=300):
    print(f"{name} enrolled in {course} — Fee: {fee} BDT")

enroll_student("Ayman")
# Ayman enrolled in Applied AI — Fee: 300 BDT

enroll_student("Rafi", "Deep Learning")
# Rafi enrolled in Deep Learning — Fee: 300 BDT

enroll_student("Nila", "NLP", 8000)
# Nila enrolled in NLP — Fee: 8000 BDT


# ════════════════════════════════════════════════════════════════
# SECTION 5: Keyword Arguments
# ════════════════════════════════════════════════════════════════

# Keyword arguments let you pass values by parameter name
# Order does not matter when using keyword arguments
def student_profile(name, age, gpa):
    print(f"Name: {name} | Age: {age} | GPA: {gpa}")

# Passing in different order using keyword arguments
student_profile(gpa=3.85, name="Ayman", age=23)
# Name: Ayman | Age: 23 | GPA: 3.85

# Mixing positional and keyword — positional must come first
student_profile("Rafi", gpa=3.5, age=25)
# Name: Rafi | Age: 25 | GPA: 3.5


# ════════════════════════════════════════════════════════════════
# SECTION 6: Multiple Return Values
# ════════════════════════════════════════════════════════════════

# Python functions can return multiple values as a tuple
def get_student_stats(scores):
    highest = max(scores)
    lowest  = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average         # returns a tuple

scores = [85, 92, 78, 95, 60]
high, low, avg = get_student_stats(scores)  # tuple unpacking

print(high)                                 # 95
print(low)                                  # 60
print(avg)                                  # 82.0


# ════════════════════════════════════════════════════════════════
# SECTION 7: *args — Multiple Positional Arguments
# ════════════════════════════════════════════════════════════════

# *args collects any number of positional arguments into a tuple
# Useful when you don't know how many arguments will be passed
def total_marks(*args):
    print(f"Received scores: {args}")       # args is a tuple
    return sum(args)

print(total_marks(80, 90))                  # Received scores: (80, 90)
                                            # 170

print(total_marks(70, 85, 90, 95))          # Received scores: (70, 85, 90, 95)
                                            # 340


# ════════════════════════════════════════════════════════════════
# SECTION 8: **kwargs — Multiple Keyword Arguments
# ════════════════════════════════════════════════════════════════

# **kwargs collects any number of keyword arguments into a dictionary
# Very common in ML libraries like PyTorch, Keras for model configs
def build_model_config(**kwargs):
    print("Model Configuration:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

build_model_config(
    model    = "Neural Network",
    layers   = 5,
    dropout  = 0.3,
    optimizer= "Adam"
)
# Model Configuration:
#   model: Neural Network
#   layers: 5
#   dropout: 0.3
#   optimizer: Adam


# ════════════════════════════════════════════════════════════════
# SECTION 9: *args + **kwargs Together
# ════════════════════════════════════════════════════════════════

# Combining both — maximum flexibility
# Order must be: normal params → *args → **kwargs
def train_model(model_name, *scores, **config):
    print(f"Training: {model_name}")
    print(f"Scores: {scores}")
    print(f"Config: {config}")

train_model(
    "ResNet",
    85, 90, 78,
    epochs=10,
    lr=0.001
)
# Training: ResNet
# Scores: (85, 90, 78)
# Config: {'epochs': 10, 'lr': 0.001}


# ════════════════════════════════════════════════════════════════
# SECTION 10: Separator in print()
# ════════════════════════════════════════════════════════════════

# sep parameter defines what goes between multiple print values
# Default sep is a single space " "
def display_student(name, age, gpa):
    print(name, age, gpa, sep=" | ")

display_student("Ayman", 23, 3.85)          # Ayman | 23 | 3.85
display_student("Rafi",  25, 3.50)          # Rafi | 25 | 3.50

# sep and end combined
print("Name", "Age", "GPA", sep="-", end="\n---\n")
# Name-Age-GPA
# ---


# ════════════════════════════════════════════════════════════════
# SECTION 11: Input from User + Type Casting
# ════════════════════════════════════════════════════════════════

# input() always returns a STRING — must cast to correct type
# int() converts string to integer
# float() converts string to float
# str() converts anything to string
# bool() converts to boolean

def get_student_input():
    name = input("Enter student name: ")        # str by default
    age  = int(input("Enter age: "))            # cast to int
    gpa  = float(input("Enter GPA: "))          # cast to float

    print(f"\n--- Student Profile ---")
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"GPA  : {gpa}")
    print(f"Types: {type(name)}, {type(age)}, {type(gpa)}")

    # Eligibility check using the collected data
    if age >= 18 and gpa >= 2.5:
        print("Status: Eligible for enrollment")
    else:
        print("Status: Not eligible")

get_student_input()

# Enter student name: Ayman
# Enter age: 23
# Enter GPA: 3.85
#
# --- Student Profile ---
# Name : Ayman
# Age  : 23
# GPA  : 3.85
# Types: <class 'str'>, <class 'int'>, <class 'float'>
# Status: Eligible for enrollment


# ════════════════════════════════════════════════════════════════
# SECTION 12: Type Casting — Deep Dive
# ════════════════════════════════════════════════════════════════

# Explicit type conversion between compatible types
def type_casting_demo():
    # String to number
    age_str = "23"
    age_int = int(age_str)                  # "23" → 23
    age_flt = float(age_str)               # "23" → 23.0

    # Number to string
    gpa       = 3.85
    gpa_str   = str(gpa)                   # 3.85 → "3.85"

    # Float to int — truncates decimal (does NOT round)
    score     = 87.9
    score_int = int(score)                 # 87.9 → 87 (not 88!)

    # Bool casting
    print(bool(0))                         # False
    print(bool(1))                         # True
    print(bool(""))                        # False
    print(bool("Ayman"))                   # True
    print(bool(None))                      # False

    print(age_int, type(age_int))          # 23 <class 'int'>
    print(age_flt, type(age_flt))          # 23.0 <class 'float'>
    print(gpa_str, type(gpa_str))          # 3.85 <class 'str'>
    print(score_int, type(score_int))      # 87 <class 'int'>

type_casting_demo()