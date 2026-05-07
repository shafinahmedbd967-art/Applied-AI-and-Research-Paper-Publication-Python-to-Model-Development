# a basic list to get started
fruits = ["apple", "banana", "mango", "orange"]

print(fruits)
# Output: ['apple', 'banana', 'mango', 'orange']

print(fruits[0])
# Output: apple

print(fruits[-1])
# Output: orange

# slicing - getting a portion of the list
print(fruits[1:3])
# Output: ['banana', 'mango']


# lists are mutable, so we can change items
fruits[1] = "grape"
print(fruits)
# Output: ['apple', 'grape', 'mango', 'orange']


# common list methods
fruits.append("watermelon")   # adds to the end
print(fruits)
# Output: ['apple', 'grape', 'mango', 'orange', 'watermelon']

fruits.remove("grape")        # removes by value
print(fruits)
# Output: ['apple', 'mango', 'orange', 'watermelon']

popped = fruits.pop()         # removes and returns the last item
print(popped)
# Output: watermelon

print(len(fruits))
# Output: 3


# lists can hold mixed types
mixed = [1, "hello", 3.14, True]
print(mixed)
# Output: [1, 'hello', 3.14, True]


# nested list - list inside a list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])
# Output: 6


# looping through a list
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)
# Output:
# 10
# 20
# 30
# 40


# list comprehension - shorter way to build a list
squares = [x ** 2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

# with a condition inside comprehension
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)
# Output: [4, 16, 36, 64, 100]


# sorting a list
scores = [55, 90, 23, 78, 45]
scores.sort()
print(scores)
# Output: [23, 45, 55, 78, 90]

scores.sort(reverse=True)
print(scores)
# Output: [90, 78, 55, 45, 23]


# *args section - for multiple positional arguments
# this function doesnt know how many numbers it will receive
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))
# Output: 6

print(add_all(10, 20, 30, 40, 50))
# Output: 150

# args is just a tuple inside the function
def show_args(*args):
    print(type(args))
    print(args)

show_args(5, "hello", True)
# Output: <class 'tuple'>
# Output: (5, 'hello', True)


# mixing normal parameter with args
def greet(greeting, *names):
    for name in names:
        print(greeting, name)

greet("Hello", "Rahim", "Karim", "Jamal")
# Output: Hello Rahim
# Output: Hello Karim
# Output: Hello Jamal


# unpacking a list into a function using *
def multiply(a, b, c):
    return a * b * c

values = [2, 3, 4]
result = multiply(*values)
print(result)
# Output: 24


# **kwargs section

# kwargs collects named arguments into a dictionary
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Rahim", age=25, city="Dhaka")
# Output: name : Rahim
# Output: age : 25
# Output: city : Dhaka


# checking the type of kwargs inside the function
def check_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

check_kwargs(language="Python", level="beginner")
# Output: <class 'dict'>
# Output: {'language': 'Python', 'level': 'beginner'}


# practical use case - building a user profile dynamically
def create_profile(name, **kwargs):
    profile = {"name": name}
    profile.update(kwargs)
    return profile

p = create_profile("Karim", age=30, job="engineer", city="Chittagong")
print(p)
# Output: {'name': 'Karim', 'age': 30, 'job': 'engineer', 'city': 'Chittagong'}


# unpacking a dictionary into a function using **
def introduce(name, age, city):
    print("My name is", name, "I am", age, "years old and I live in", city)

data = {"name": "Jamal", "age": 22, "city": "Sylhet"}
introduce(**data)
# Output: My name is Jamal I am 22 years old and I live in Sylhet


# ----- combining normal args kwargs together -----

# order must be: normal params first, then *args, then **kwargs
def full_example(role, *args, **kwargs):
    print("Role:", role)
    print("Extra positional args:", args)
    print("Keyword args:", kwargs)

full_example("admin", "read", "write", username="rahim", level=3)
# Output: Role: admin
# Output: Extra positional args: ('read', 'write')
# Output: Keyword args: {'username': 'rahim', 'level': 3}


# real world example - a logging function
def log_event(event_type, *messages, **metadata):
    print("Event:", event_type)
    for msg in messages:
        print("  Message:", msg)
    for key, value in metadata.items():
        print("  " + key + ":", value)

log_event(
    "ERROR",
    "Database connection failed",
    "Retrying in 5 seconds",
    module="db_handler",
    line=42
)
# Output: Event: ERROR
# Output:   Message: Database connection failed
# Output:   Message: Retrying in 5 seconds
# Output:   module: db_handler
# Output:   line: 42