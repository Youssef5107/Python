# =====================================================
# PYTHON CONTROL FLOW & LOOPS COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: CONDITIONALS (IF, ELIF, ELSE)
# =====================================================

# 1. BASIC IF-ELIF-ELSE STATEMENTS (Most Common)
# Evaluating conditions sequentially to execute code paths.
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This block executes
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# 2. TERNARY CONDITIONAL OPERATORS (Very Common)
# Inline conditional assignment for shorthand logic.
# syntax: [on_true] if [condition] else [on_false]
status = "Adult" if age >= 18 else "Minor"


# =====================================================
# PART 2: PATTERN MATCHING (SWITCH / CASE)
# =====================================================

# 1. STRUCTURAL PATTERN MATCHING / MATCH-CASE (Common in Python 3.10+)
# Replaces traditional switch-case structures found in other languages.
http_status = 404

match http_status:
    case 200:
        print("Success")
    case 400 | 401:                              # Combining patterns using pipe (|)
        print("Client Error")
    case 404:
        print("Not Found")                      # This block executes
    case _ :                                     # Wildcard catch-all (default case)
        print("Unknown Status Code")


# =====================================================
# PART 3: FOR LOOPS (ITERATION)
# =====================================================

# 1. FOR IN LOOPS WITH ITERABLES / RANGE (Most Common)
# Iterating over sequences (lists, strings, ranges).
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i in range(3):                               # Generates numbers: 0, 1, 2
    print(i)


# 2. ENUMERATE & ZIP LOOPS (Very Common)
# Tracking indices while looping, or iterating over multiple lists in parallel.
names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]

# Using enumerate to get both index and value
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

# Using zip to loop through multiple collections together
for name, score in zip(names, scores):
    print(f"{name} scored {score}")


# =====================================================
# PART 4: WHILE LOOPS
# =====================================================

# 1. CONDITIONAL WHILE LOOPS (Very Common)
# Repeating a block of code as long as a condition evaluates to True.
counter = 3
while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1


# =====================================================
# PART 5: LOOP CONTROL STATEMENTS (BREAK, CONTINUE, ELSE)
# =====================================================

# 1. BREAK & CONTINUE (Very Common)
# Modifying loop execution flow.
for num in range(5):
    if num == 2:
        continue        # Skips iteration when num is 2
    if num == 4:
        break           # Terminates the loop completely
    print(num)


# 2. FOR-ELSE / WHILE-ELSE BLOCKS (Less Common)
# The `else` block runs only if the loop finishes *without* hitting a `break`.
for num in range(3):
    if num == 99:
        break
else:
    print("Loop completed successfully without breaking!")


# =====================================================
# PART 6: "DO-WHILE" EQUIVALENTS IN PYTHON
# =====================================================

# Python does not have a native `do-while` loop syntax. 
# Instead, developers emulate it using a `while True` loop with a `break` condition.

# Emulated Do-While Loop (Executes at least once before checking condition)
password = ""
while True:
    password = "secure_password_123"  # Simulated user input step
    if password == "secure_password_123":
        print("Access Granted")
        break
    print("Incorrect password, try again.")