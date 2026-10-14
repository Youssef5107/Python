# =====================================================
# PYTHON VARIABLES & FUNCTIONS COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: VARIABLES
# =====================================================

# 1. BASIC VARIABLE ASSIGNMENT (Most Common)
# Storing data in memory using names. Python uses dynamic typing (no type declaration needed).
age = 25                  # Integer
price = 19.99             # Float
name = "Youssef"          # String
is_active = True          # Boolean


# 2. MULTIPLE & CHAINED ASSIGNMENT (Very Common)
# Assigning multiple variables in a single line.
x, y, z = 10, 20, 30      # Multiple assignment
a = b = c = 100           # Chained assignment


# 3. VARIABLE REASSIGNMENT & UPDATING (Very Common)
# Changing the value or data type of a variable over time.
score = 50
score = score + 10        # Updates score to 60
score += 10               # Shorthand operator (also -=, *=, /=)


# 4. VARIABLE SCOPE: LOCAL VS GLOBAL (Common)
# Where variables can be accessed in your code.
global_var = "I am global"  # Accessible anywhere in the file

def check_scope():
    local_var = "I am local"  # Only accessible inside this function
    print(global_var)         # Can read global variables inside functions

# print(local_var)          # Error! local_var doesn't exist outside the function.


# =====================================================
# PART 2: FUNCTIONS & METHODS
# =====================================================

# 1. BASIC FUNCTION DEFINITION & CALLING (Most Common)
# Reusable blocks of code using the `def` keyword.
def say_hello():
    print("Hello, World!")

say_hello()  # Calling the function


# 2. FUNCTIONS WITH PARAMETERS & RETURN VALUES (Most Common)
# Passing inputs into functions and returning outputs using `return`.
def add_numbers(num1, num2):
    result = num1 + num2
    return result

sum_result = add_numbers(5, 10)  # sum_result is 15


# 3. DEFAULT & KEYWORD ARGUMENTS (Very Common)
# Providing fallback values if an argument isn't provided when called.
def connect_to_server(host, port=80):
    print(f"Connecting to {host}:{port}")

connect_to_server("192.168.1.1")          # Uses default port 80
connect_to_server("192.168.1.1", port=443)  # Uses keyword argument override


# 4. ARBITRARY ARGUMENTS: *args AND **kwargs (Common)
# Accepting an unknown number of positional (*args) or keyword (**kwargs) arguments.
def print_network_devices(*devices, **settings):
    print("Devices:", devices)   # Handled as a tuple
    print("Settings:", settings) # Handled as a dictionary

print_network_devices("Router", "Switch", timeout=30, verbose=True)


# 5. LAMBDA (ANONYMOUS) FUNCTIONS (Less Common)
# Small, one-line unnamed functions often used for short operations or sorting.
square = lambda x: x ** 2
print(square(5))  # Outputs: 25


# 6. TYPE HINTS & DOCSTRINGS (Less Common / Professional)
# Documenting function behavior and expected data types for better code maintainability.
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given length and width."""
    return length * width


# 7. NESTED FUNCTIONS & CLOSURES (Least Common / Advanced)
# Defining a function inside another function to encapsulate logic.
def outer_function(text):
    def inner_function():
        print(f"Nested output: {text}")
    return inner_function

my_closure = outer_function("Hello from closure")
my_closure()  # Executes inner function