# 02_variable_comparison_student_age.py

# ─── Student Data ────────────────────────────────────────────────────────
student_1_name = "Ayman"
student_1_age = 23

student_2_name = "Rafi"
student_2_age = 25

student_3_name = "Nila"
student_3_age = 23

MINIMUM_AGE = 18
MAXIMUM_AGE = 30


# ─── Basic Comparison ────────────────────────────────────────────────────
print(student_1_age == student_2_age)       # False
print(student_1_age == student_3_age)       # True
print(student_1_age != student_2_age)       # True
print(student_1_age > student_2_age)        # False
print(student_1_age < student_2_age)        # True
print(student_1_age >= student_3_age)       # True
print(student_1_age <= student_2_age)       # True


# ─── Eligibility Check ───────────────────────────────────────────────────
is_ayman_eligible = MINIMUM_AGE <= student_1_age <= MAXIMUM_AGE
is_rafi_eligible  = MINIMUM_AGE <= student_2_age <= MAXIMUM_AGE

print(is_ayman_eligible)                    # True
print(is_rafi_eligible)                     # True


# ─── Who is Older ────────────────────────────────────────────────────────
is_ayman_older = student_1_age > student_2_age
is_rafi_older  = student_2_age > student_1_age
is_same_age    = student_1_age == student_2_age

print(is_ayman_older)                       # False
print(is_rafi_older)                        # True
print(is_same_age)                          # False


# ─── Comparing with String ───────────────────────────────────────────────
print(student_1_name == student_2_name)     # False
print(student_1_name == "Ayman")            # True
print(student_1_name != student_2_name)     # True


# ─── Age Difference ──────────────────────────────────────────────────────
age_difference = student_2_age - student_1_age
print(age_difference)                       # 2
print(age_difference > 0)                   # True  (Rafi is older)
print(age_difference == 0)                  # False (not same age)


# ─── Chained Comparison ──────────────────────────────────────────────────
# Python allows chaining comparisons — very clean and readable
print(student_1_age < student_2_age < 30)   # True
print(18 < student_1_age < 25)              # True
print(18 < student_2_age < 24)              # False  (25 is not < 24)


# ─── Comparing Result Stored in Variable ────────────────────────────────
ayman_is_adult   = student_1_age >= 18
rafi_is_adult    = student_2_age >= 18
both_are_adults  = ayman_is_adult == rafi_is_adult

print(ayman_is_adult)                       # True
print(rafi_is_adult)                        # True
print(both_are_adults)                      # True


# ─── is vs == ────────────────────────────────────────────────────────────
# == checks VALUE equality
# is checks IDENTITY (same memory address / same object)

a = 23
b = 23
print(a == b)                               # True  (same value)
print(a is b)                               # True  (Python caches small ints)

x = 1000
y = 1000
print(x == y)                               # True  (same value)
print(x is y)                               # False (different objects in memory) 