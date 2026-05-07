#Basic Variable Assignment────
name = "Ayman"          # str type
age = 23                # int type
gpa = 3.85              # float type
is_enrolled = True      # bool type

print(name)             # Ayman
print(age)              # 23
print(gpa)              # 3.85
print(is_enrolled)      # True


#type() to Check Data Types
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(is_enrolled)) # <class 'bool'>


# Dynamic Typing
x = 10
print(type(x))          # <class 'int'>

x = "hello"
print(type(x))          # <class 'str'>

x = 3.14
print(type(x))          # <class 'float'>


# Multiple Assignment
# Assign multiple variables at once
a, b, c = 1, 2, 3
print(a, b, c)          # 1 2 3

# Assign the same value to multiple variables
p = q = r = 0
print(p, q, r)          # 0 0 0


# id() to Check Memory Address 
# Variable actually references an object in memory. Small integers are cached by Python, so they may have the same id.
m = 10
n = 10
print(id(m))            # 140234567891234  (example — same object!)
print(id(n))            # 140234567891234  (Python do small int cacheing)

# but large numbers or mutable objects have different addresses
p = 99999
q = 99999
print(id(p) == id(q))   # False (most likely different objects)


# ─── Variable Swapping ───────────────────────────────────────────────────
# In another language, you might need a temporary variable to swap values. In Python, you can swap directly.
x = 5
y = 10
x, y = y, x
print(x, y)             # 10 5


# ─── Constants (Convention) ──────────────────────────────────────────────
# iN PYTHON, there is no built-in constant type, but by convention, we use uppercase variable names to indicate that they should not be changed.
LEARNING_RATE = 0.001
MAX_EPOCHS = 100
print(LEARNING_RATE)    # 0.001
print(MAX_EPOCHS)       # 100


# ─── del to Delete Variables ─────────────────────────────────────────────
temp = "I am temporary"
print(temp)             # I am temporary
del temp
# print(temp)           # NameError: name 'temp' is not defined