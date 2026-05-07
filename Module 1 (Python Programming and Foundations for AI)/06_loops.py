#  SECTION 1: range() — The Core Tool for Looping
# range(stop)          → 0 to stop-1
# range(start, stop)   → start to stop-1
# range(start, stop, step) → start to stop-1 with step

print(list(range(5)))               # [0, 1, 2, 3, 4]
print(list(range(1, 6)))            # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))        # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1)))       # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#  SECTION 2: for Loop with range()
# Basic for loop — runs exactly 5 times
for i in range(5):
    print(i, end=" ")               # 0 1 2 3 4
print()

# Looping through student scores
scores = [85, 92, 78, 95, 60]

total = 0
for score in scores:
    total += score                  # accumulating total
print(f"Total: {total}")            # Total: 410
print(f"Average: {total / len(scores)}")  # Average: 82.0

# Loop with start and step
print("Even numbers from 2 to 10:")
for num in range(2, 11, 2):
    print(num, end=" ")             # 2 4 6 8 10
print()

# Reverse loop
print("Countdown:")
for i in range(5, 0, -1):
    print(i, end=" ")               # 5 4 3 2 1
print()


# ════════════════════════════════════════════════════════════════
# SECTION 3: for Loop over List, String
# ════════════════════════════════════════════════════════════════

# Iterating over a list of student names
students = ["Ayman", "Rafi", "Nila", "Sara"]

for student in students:
    print(f"Hello, {student}!")
# Hello, Ayman!
# Hello, Rafi!
# Hello, Nila!
# Hello, Sara!

# Iterating over a string — character by character
name = "Ayman"
for char in name:
    print(char, end="-")            # A-y-m-a-n-
print()


#  SECTION 4: enumerate() — Index + Value Together
# enumerate() gives both the index and the value at the same time
# Without enumerate — manually tracking index (bad practice)
students = ["Ayman", "Rafi", "Nila", "Sara"]

for i in range(len(students)):
    print(i, students[i])           # works but not pythonic
# 0 Ayman
# 1 Rafi
# 2 Nila
# 3 Sara

print()

# With enumerate — clean and pythonic
for index, student in enumerate(students):
    print(f"{index}: {student}")
# 0: Ayman
# 1: Rafi
# 2: Nila
# 3: Sara

print()

# enumerate() with custom start index
for index, student in enumerate(students, start=1):
    print(f"Student {index}: {student}")
# Student 1: Ayman
# Student 2: Rafi
# Student 3: Nila
# Student 4: Sara

print()

# Real use case — finding rank based on score
scores = [85, 92, 78, 95]
students = ["Ayman", "Rafi", "Nila", "Sara"]

print("Score Report:")
for index, (student, score) in enumerate(zip(students, scores), start=1):
    print(f"Rank {index} | {student}: {score}")
# Rank 1 | Ayman: 85
# Rank 2 | Rafi: 92
# Rank 3 | Nila: 78
# Rank 4 | Sara: 95


#  SECTION 5: while Loop
# while loop runs as long as the condition is True
# Use when you don't know how many iterations are needed

count = 0
while count < 5:
    print(count, end=" ")           # 0 1 2 3 4
    count += 1                      # must update — otherwise infinite loop
print()

# Simulating training epochs with while loop
epoch        = 1
max_epochs   = 5
loss         = 1.0

while epoch <= max_epochs:
    loss = loss * 0.7               # loss decreasing each epoch
    print(f"Epoch {epoch} | Loss: {loss:.4f}")
    epoch += 1
# Epoch 1 | Loss: 0.7000
# Epoch 2 | Loss: 0.4900
# Epoch 3 | Loss: 0.3430
# Epoch 4 | Loss: 0.2401
# Epoch 5 | Loss: 0.1681


#  SECTION 6: break and continue

# break — exits the loop immediately
print("Break example:")
for i in range(10):
    if i == 5:
        break                       # stops when i reaches 5
    print(i, end=" ")               # 0 1 2 3 4
print()

# continue — skips current iteration and moves to next
print("Continue example:")
for i in range(10):
    if i % 2 == 0:
        continue                    # skips even numbers
    print(i, end=" ")               # 1 3 5 7 9
print()

# Real use case — skip failed scores, stop at perfect score
scores = [72, 85, -1, 91, 100, 60]

for score in scores:
    if score == -1:
        print("Invalid score found — skipping")
        continue                    # skip invalid entry
    if score == 100:
        print(f"Perfect score {score} found — stopping")
        break                       # stop at perfect score
    print(f"Score: {score}")

# Score: 72
# Score: 85
# Invalid score found — skipping
# Score: 91
# Perfect score 100 found — stopping




#  SECTION 7: while with break — Input Validation Loop
# Keep asking for input until valid data is provided
# This is a very common real-world pattern

def get_valid_age():
    while True:                     # runs forever until break
        age = int(input("Enter student age (18-30): "))
        if 18 <= age <= 30:
            print(f"Valid age: {age}")
            break                   # exit loop on valid input
        else:
            print("Invalid age. Try again.")

# get_valid_age()
# Enter student age (18-30): 10  → Invalid age. Try again.
# Enter student age (18-30): 25  → Valid age: 25


#  SECTION 8: Nested Loops
# A loop inside another loop
# Outer loop runs N times, inner loop runs M times → N×M total iterations

students = ["Ayman", "Rafi"]
subjects = ["Math", "AI", "Python"]

for student in students:
    for subject in subjects:
        print(f"{student} → {subject}")
# Ayman → Math
# Ayman → AI
# Ayman → Python
# Rafi  → Math
# Rafi  → AI
# Rafi  → Python



#   SECTION 9: List Comprehension — Pythonic Loop
# One-line loop that builds a list — extremely common in ML/data processing
# Syntax: [expression for item in iterable if condition]

scores = [85, 92, 78, 95, 60]

# Normal loop version
passed = []
for score in scores:
    if score >= 70:
        passed.append(score)

# List comprehension version — same result
passed = [score for score in scores if score >= 70]
print(passed)                       # [85, 92, 78, 95]

# Squaring all scores
squared = [score ** 2 for score in scores]
print(squared)                      # [7225, 8464, 6084, 9025, 3600]

# Normalize scores to 0-1 range (common in ML preprocessing)
max_score  = max(scores)
normalized = [round(score / max_score, 2) for score in scores]
print(normalized)                   # [0.89, 0.97, 0.82, 1.0, 0.63]