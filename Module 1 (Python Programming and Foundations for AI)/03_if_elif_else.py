# Basic if / else 
age = 20

if age >= 18:
    print("Adult")                          # Adult
else:
    print("Minor")


# if / elif / else
score = 72

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(grade)                                # B


# ─── Student Age Eligibility ─────────────────────────────────────────────
student_name = "Ayman"
student_age  = 23
MINIMUM_AGE  = 18
MAXIMUM_AGE  = 30

if student_age < MINIMUM_AGE:
    print(f"{student_name} is too young to enroll")
elif student_age > MAXIMUM_AGE:
    print(f"{student_name} is too old for this program")
else:
    print(f"{student_name} is eligible to enroll") # Ayman is eligible to enroll


# ─── Nested if ───────────────────────────────────────────────────────────
# if in an if
student_gpa    = 3.85
has_documents  = True

if student_age >= MINIMUM_AGE:
    if student_gpa >= 3.5:
        if has_documents:
            print("Eligible for scholarship")   # Eligible for scholarship
        else:
            print("Submit documents first")
    else:
        print("GPA too low for scholarship")
else:
    print("Age requirement not met")


# ─── Multiple Conditions with and / or / not ─────────────────────────────
is_enrolled    = True
has_paid_fee   = False
is_verified    = True

# all conditions must be True
if is_enrolled and has_paid_fee and is_verified:
    print("Full access granted")
else:
    print("Access denied — check enrollment, fee, or verification")
    # Access denied — check enrollment, fee, or verification

# or — any one condition is True, the whole expression is True
has_scholarship = False
has_waiver      = True

if has_scholarship or has_waiver:
    print("Fee exempted")                       # Fee exempted

# not — flip the boolean value
if not has_paid_fee:
    print("Payment pending")                    # Payment pending


# ─── Comparing Multiple Students ─────────────────────────────────────────
student_1_age = 23
student_2_age = 25
student_3_age = 16

students = {
    "Ayman" : student_1_age,
    "Rafi"  : student_2_age,
    "Nila"  : student_3_age
}

for name, age in students.items():
    if age >= MINIMUM_AGE and age <= MAXIMUM_AGE:
        status = "Eligible"
    else:
        status = "Not Eligible"
    print(f"{name} (age {age}): {status}")

# Ayman (age 23): Eligible
# Rafi  (age 25): Eligible
# Nila  (age 16): Not Eligible


# ─── Ternary Operator (one-liner if else) ────────────────────────────────
# condition occurs value_1, otherwise value_2
age    = 20
status = "Adult" if age >= 18 else "Minor"
print(status)                               # Adult


# ─── if with None check ──────────────────────────────────────────────────
student_email = None

if student_email is None:
    print("No email provided")              # No email provided
else:
    print(f"Email: {student_email}")


# ─── Truthy and Falsy ────────────────────────────────────────────────────
# In Python, certain values are considered "falsy" (evaluate to False in a boolean context), while others are "truthy" (evaluate to True).
empty_name   = ""
filled_name  = "Ayman"
zero_age     = 0
valid_age    = 23

if empty_name:
    print("Has name")
else:
    print("Name is empty")                  # Name is empty

if filled_name:
    print(f"Student: {filled_name}")        # Student: Ayman

if zero_age:
    print("Has age")
else:
    print("Age is zero or not set")         # Age is zero or not set

if valid_age:
    print(f"Age is: {valid_age}")           # Age is: 23
