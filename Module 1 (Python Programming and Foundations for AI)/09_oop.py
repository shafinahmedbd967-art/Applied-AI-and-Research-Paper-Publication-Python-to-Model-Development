# a simple class definition - this is just a blueprint, not an actual object
class Dog:

    # this runs automatically when a new object is created
    def __init__(self, name, breed, age):
        self.name = name      # instance variable - belongs to each object
        self.breed = breed
        self.age = age

    def bark(self):
        print(self.name, "says: Woof!")

    def info(self):
        print(self.name, "is a", self.breed, "and is", self.age, "years old")

# creating objects from the class
dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)

dog1.bark()
# Output: Bruno says: Woof!

dog2.info()
# Output: Max is a Poodle and is 5 years old

# each object has its own data
print(dog1.name, dog2.name)
# Output: Bruno Max


# how many objects? as many as you want
dog3 = Dog("Tommy", "Bulldog", 2)
dog4 = Dog("Rocky", "Husky", 4)
print(dog3.name, dog4.name)
# Output: Tommy Rocky


# We can also pass arguments when creating objects just like a normal function
def make_dog(name, breed, age):
    return Dog(name, breed, age)

dog5 = make_dog("Buddy", "Beagle", 1)
dog5.info()
# Output: Buddy is a Beagle and is 1 years old


# encapsulation and private variables - using __ to make a variable private (not accessible from outside)
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # private variable - cant be accessed directly from outside

    # getter method - controlled way to read private data
    def get_balance(self):
        return self.__balance

    # setter method - controlled way to change private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)


account = BankAccount("Rahim", 5000)

# this would cause an error - private variable cant be accessed directly
# print(account.__balance)

# correct way - use the method
print(account.get_balance())
# Output: 5000

account.deposit(2000)
# Output: Deposited: 2000

print(account.get_balance())
# Output: 7000

account.withdraw(10000)
# Output: Not enough balance


# ----- inheritance -----

# parent class
class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(self.name, "says", self.sound)

    def breathe(self):
        print(self.name, "is breathing")


# child class inherits everything from Animal
class Cat(Animal):

    def __init__(self, name):
        super().__init__(name, "Meow")   # calling parent constructor
        self.lives = 9

    def show_lives(self):
        print(self.name, "has", self.lives, "lives")


class Bird(Animal):

    def __init__(self, name):
        super().__init__(name, "Tweet")
        self.can_fly = True

    def fly(self):
        if self.can_fly:
            print(self.name, "is flying")


cat = Cat("Whiskers")
cat.speak()         # inherited from Animal
# Output: Whiskers says Meow

cat.breathe()       # inherited from Animal
# Output: Whiskers is breathing

cat.show_lives()    # defined in Cat
# Output: Whiskers has 9 lives

bird = Bird("Tweety")
bird.speak()
# Output: Tweety says Tweet

bird.fly()
# Output: Tweety is flying


# multi-level inheritance - grandparent to parent to child
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "engine started")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print("Driving", self.brand, self.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def charge(self):
        print("Charging battery:", self.battery, "kWh")


tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.start()     # from Vehicle
# Output: Tesla engine started

tesla.drive()     # from Car
# Output: Driving Tesla Model 3

tesla.charge()    # from ElectricCar
# Output: Charging battery: 75 kWh


# polymorphism - same method name, different behavior in different classes

class Dog2:
    def speak(self):
        return "Woof!"

class Cat2:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"


# polymorphism in action - we dont care what type it is, just call speak()
animals = [Dog2(), Cat2(), Duck()]
for animal in animals:
    print(animal.speak())
# Output: Woof!
# Output: Meow!
# Output: Quack!


# method overriding - child changes parent behavior
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):           # overriding the parent method
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):           # overriding the parent method
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())
# Output: 78.53975
# Output: 24


# static methods 

class MathHelper:

    # no self needed - this doesnt depend on any object
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# calling static method without creating any object
print(MathHelper.add(10, 20))
# Output: 30

print(MathHelper.is_even(7))
# Output: False

print(MathHelper.celsius_to_fahrenheit(100))
# Output: 212.0

# static methods can also be called on an object but its not common
m = MathHelper()
print(m.add(3, 4))
# Output: 7


# ----- class variable (shared across all objects) -----

class Student:

    school_name = "Dhaka University"   # class variable - shared by all objects
    total_students = 0

    def __init__(self, name, roll):
        self.name = name               # instance variable - unique per object
        self.roll = roll
        Student.total_students += 1    # update shared counter every time a student is made

    def show(self):
        print(self.name, "| Roll:", self.roll, "| School:", Student.school_name)


s1 = Student("Rahim", 101)
s2 = Student("Karim", 102)
s3 = Student("Jamal", 103)

s1.show()
# Output: Rahim | Roll: 101 | School: Dhaka University

print("Total students:", Student.total_students)
# Output: Total students: 3


# magic methods
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # called when we print the object - human readable
    def __str__(self):
        return self.title + " by " + self.author

    # called when we just type the object in console - developer readable
    def __repr__(self):
        return "Book('" + self.title + "', '" + self.author + "', " + str(self.pages) + ")"

    # called when we use len()
    def __len__(self):
        return self.pages

    # called when we use == to compare two objects
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # called when we use + operator
    def __add__(self, other):
        combined_title = self.title + " & " + other.title
        return Book(combined_title, "Various", self.pages + other.pages)

    # called when we use < operator
    def __lt__(self, other):
        return self.pages < other.pages


book1 = Book("Python Basics", "Rahim", 300)
book2 = Book("AI Fundamentals", "Karim", 450)
book3 = Book("Python Basics", "Rahim", 300)

print(book1)
# Output: Python Basics by Rahim

print(repr(book1))
# Output: Book('Python Basics', 'Rahim', 300)

print(len(book1))
# Output: 300

print(book1 == book3)   # same title and author
# Output: True

print(book1 == book2)
# Output: False

combined = book1 + book2
print(combined)
# Output: Python Basics & AI Fundamentals by Various
print(len(combined))
# Output: 750

print(book1 < book2)   # 300 < 450
# Output: True


# sorting works automatically once __lt__ is defined
books = [book2, book1, Book("ML Guide", "Jamal", 200)]
books.sort()
for b in books:
    print(b, "-", len(b), "pages")
# Output: ML Guide by Jamal - 200 pages
# Output: Python Basics by Rahim - 300 pages
# Output: AI Fundamentals by Karim - 450 pages


# ----- a complete real world example putting it all together -----

class Employee:

    company = "TechCorp BD"
    total_employees = 0

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary        # private - salary is sensitive
        Employee.total_employees += 1

    def get_salary(self):
        return self.__salary

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
            print(self.name, "got a raise of", amount)

    @staticmethod
    def company_policy():
        print("Work hard, stay honest.")

    def __str__(self):
        return self.name + " (" + self.role + ") at " + Employee.company

    def __repr__(self):
        return "Employee('" + self.name + "', '" + self.role + "')"


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, "Manager", salary)
        self.team_size = team_size

    def show_team(self):
        print(self.name, "manages a team of", self.team_size, "people")


class Intern(Employee):

    def __init__(self, name, salary, duration_months):
        super().__init__(name, "Intern", salary)
        self.duration = duration_months

    def show_duration(self):
        print(self.name, "is interning for", self.duration, "months")


e1 = Manager("Rahim", 80000, 10)
e2 = Intern("Karim", 15000, 6)

print(e1)
# Output: Rahim (Manager) at TechCorp BD

print(e2)
# Output: Karim (Intern) at TechCorp BD

e1.give_raise(10000)
# Output: Rahim got a raise of 10000

print(e1.get_salary())
# Output: 90000

e1.show_team()
# Output: Rahim manages a team of 10 people

e2.show_duration()
# Output: Karim is interning for 6 months

Employee.company_policy()
# Output: Work hard, stay honest.

print("Total employees:", Employee.total_employees)
# Output: Total employees: 2

# polymorphism - both are employees, but behave differently
team = [e1, e2]
for member in team:
    print(repr(member))
# Output: Employee('Rahim', 'Manager')
# Output: Employee('Karim', 'Intern')