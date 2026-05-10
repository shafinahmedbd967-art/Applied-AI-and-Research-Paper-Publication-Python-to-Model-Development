# Module 1: Python Programming and Foundations for AI

**Course:** Applied AI and Research Paper Publication (Python to Model Development)
**Module:** 01 — Python Programming and Foundations for AI

---

## What This Module Covers

This module builds the complete Python foundation needed before moving into Machine Learning and AI development. Every topic is taught with ML use cases in mind.

---

## Topics Covered

### 01 — Variables
Declaration, dynamic typing, memory references, multiple assignment, `id()`, `del`, constants convention.

### 02 — Variable Comparison
Comparison operators, chained comparison, `==` vs `is`, storing comparison results, student age comparison example.

### 03 — if / elif / else
Conditional logic, nested if, `and` / `or` / `not`, ternary operator, truthy/falsy values, `None` check.

### 04 — end Parameter
Overriding default newline in `print()`, custom separators, inline printing.

### 05 — Functions
No-return functions, parameters, return values, default arguments, keyword arguments, multiple return values, `*args`, `**kwargs`, `*args + **kwargs`, separator in print, `input()` with type casting.

### 06 — Loops
`range()`, `for` loop, iterating over list and string, `enumerate()`, `while` loop, `break` / `continue`, nested loops, list comprehension.

### 07 — Built-in Data Structures
List (slicing, negative indexing, methods), Tuple (immutability, unpacking), List vs Tuple comparison, Dictionary (nested dict), Set (set operations), list comprehension, list comprehension in dictionary, dictionary comprehension, class-based index enumeration, when to use which structure in ML.

### 08 — Lists and Arguments
List as argument, `*args` as tuple, `**kwargs` as dictionary, unpacking with `*` and `**`, dictionary as keyword argument, ML hyperparameter config pattern.

### 09 — Object Oriented Programming
Class, object, constructor (`__init__`), `self`, instance vs class variables, encapsulation, private variables with `__`, getter and setter methods, inheritance, `super()`, multi-level inheritance, method overriding, polymorphism, static methods (`@staticmethod`), dunder and magic methods (`__str__`, `__repr__`, `__len__`, `__eq__`, `__add__`, `__lt__`).

### 10 — Error Handling
`try`, `except`, `else`, `finally`, multiple except blocks, catching exception object with `as e`, raising exceptions manually with `raise`, custom exception classes, catching all exceptions with base `Exception`, ML use cases — data loading, preprocessing, training loop, model saving, prediction validation.

### 11 — File Handling and OS Module
`open()`, `read()`, `readline()`, `readlines()`, line by line reading, `close()`, write mode `w`, append mode `a`, `with` statement and why it is safer than manual close, `os.getcwd()`, `os.path.exists()`, `os.path.isfile()`, `os.path.isdir()`, `os.mkdir()`, `os.makedirs()`, `os.path.join()`, `os.listdir()`, filtering hidden folders like `.idea`, building ML project folder structure automatically.

### 12 — Logging
`logging.basicConfig()`, five severity levels — `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, custom named logger with `getLogger()`, `FileHandler` with append and write mode, `StreamHandler`, log formatting with `asctime` / `levelname` / `message`, `logging.exception()` for full traceback, `exc_info=True`, identifying specific exception types in logs, full ML pipeline logging covering load, preprocess, train, and save steps.

---

## Key Themes Throughout This Module

- Every concept is connected to how it is actually used in ML and AI pipelines
- Error handling and logging are treated as production-level skills, not afterthoughts
- OOP is taught with real ML patterns like model classes, training loops, and encapsulated parameters
- File handling is taught with ML project folder structure in mind

---

## Folder Structure

```
Module 1 (Python Programming and Foundations for AI)/
├── 01_variables.py
├── 02_variable_comparison.py
├── 03_if_elif_else.py
├── 04_end_parameter.py
├── 05_functions.py
├── 06_loops.py
├── 07_data_structures.py
├── 08_args_kwargs.py
├── 09_oop.py
├── 10_error_handling.py
├── 11_file_handling_os.py
└── 12_logging.py
```

---

## Course Info

| | |
|---|---|
| Course | Applied AI and Research Paper Publication (Python to Model Development) |
| Module | 01 — Python Programming and Foundations for AI |
| Language | Python 3 |
| Focus | Python fundamentals with ML context |