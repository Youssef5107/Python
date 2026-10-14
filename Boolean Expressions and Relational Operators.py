# ==========================================================
# PYTHON BOOLEANS & RELATIONAL OPERATORS COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# ==========================================================


# ==========================================================
# PART 1: BOOLEAN DATA TYPES & BASIC ASSIGNMENT (Most Common)
# ==========================================================
# Booleans represent truth values: True (1) or False (0).

is_active = True
is_admin = False


# ==========================================================
# PART 2: RELATIONAL (COMPARISON) OPERATORS (Most Common)
# ==========================================================
# Used to compare two values, evaluating to a boolean (True or False).

x = 10
y = 20

equals = (x == y)          # False (Checks if equal)
not_equals = (x != y)      # True (Checks if NOT equal)
greater_than = (x > y)     # False (10 is not greater than 20)
less_than = (x < y)        # True (10 is less than 20)
greater_or_equal = (x >= y)# False 
less_or_equal = (x <= y)   # True 


# ==========================================================
# PART 3: LOGICAL OPERATORS (Very Common)
# ==========================================================
# Combining multiple boolean expressions using and, or, and not.

# 1. and (Returns True only if BOTH sides are True)
age = 25
has_id = True
can_enter = (age >= 18) and (has_id == True)  # True

# 2. or (Returns True if AT LEAST ONE side is True)
is_weekend = True
is_holiday = False
is_day_off = is_weekend or is_holiday       # True

# 3. not (Inverts the boolean value)
is_logged_in = False
is_guest = not is_logged_in                 # True


# ==========================================================
# PART 4: CONDITIONAL STATEMENTS (if / elif / else) (Very Common)
# ==========================================================
# Controlling program flow using boolean expressions.

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This block executes because 85 >= 80 is True
else:
    grade = "C"


# ==========================================================
# PART 5: TRUTHY AND FALSY VALUES (Common)
# ==========================================================
# In Python, non-boolean data types evaluate to True or False in conditions.
# Falsy values: False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict).
# Everything else is considered Truthy.

name = "Youssef"  # Non-empty string is Truthy

if name:
    print("Name exists!")


# ==========================================================
# PART 6: CHAINED COMPARISONS (Common)
# ==========================================================
# Python allows chaining relational operators cleanly.

port = 8080

# Clean chained syntax:
is_valid_web_port = (1024 <= port <= 65535)  # True

# Equivalent to: (1024 <= port) and (port <= 65535)


# ==========================================================
# PART 7: IDENTITY VS EQUALITY OPERATORS: `is` vs `==` (Less Common)
# ==========================================================
# `==` checks if values are equal.
# `is` checks if variables point to the exact same object in memory.

list_a = [1, 2, 3]
list_b = [1, 2, 3]

print(list_a == list_b)  # True (values match)
print(list_a is list_b)  # False (different objects in memory)


# ==========================================================
# PART 8: MEMBERSHIP OPERATORS: `in` and `not in` (Less Common)
# ==========================================================
# Checking if a value exists inside a sequence (strings, lists, tuples).

allowed_users = ["admin", "root", "youssef"]
user_query = "root"

is_allowed = user_query in allowed_users     # True
is_banned = "guest" not in allowed_users     # True


# ==========================================================
# PART 9: THE TERNARY CONDITIONAL OPERATOR (Least Common)
# ==========================================================
# A compact one-line if-else assignment.

user_status = "Active" if is_active else "Inactive"