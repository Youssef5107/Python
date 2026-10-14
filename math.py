# ==========================================
# PYTHON MATH COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# ==========================================


# 1. BASIC ARITHMETIC OPERATORS (Most Common)
# Standard math operations built directly into Python.
addition = 10 + 5          # 15
subtraction = 10 - 5       # 5
multiplication = 10 * 5    # 50
division = 10 / 3          # 3.3333333333333335 (Floating-point division)
floor_division = 10 // 3   # 3 (Rounds down to nearest whole number)
modulus = 10 % 3           # 1 (Remainder of division)
exponentiation = 2 ** 3    # 8 (2 to the power of 3)


# 2. BUILT-IN NUMERIC FUNCTIONS (Most Common)
# Global Python functions that work with numbers out of the box.
absolute_val = abs(-7.5)     # 7.5 (Returns absolute positive value)
highest = max(4, 12, 9)      # 12 (Returns the largest value)
lowest = min(4, 12, 9)       # 4 (Returns the smallest value)
rounded = round(5.678, 2)    # 5.68 (Rounds to specified decimal places)
squared = pow(3, 4)          # 81 (Equivalent to 3 ** 4)


# 3. THE BUILT-IN `math` MODULE (Very Common)
# Standard library module for advanced mathematical tasks. Must be imported first.
import math

# Constants
pi_val = math.pi             # 3.141592653589793
e_val = math.e               # 2.718281828459045

# Rounding & Absolute
ceiling = math.ceil(4.2)     # 5 (Rounds up to the nearest integer)
flooring = math.floor(4.8)   # 4 (Rounds down to the nearest integer)
factorial_val = math.factorial(5) # 120 (5 * 4 * 3 * 2 * 1)
sqrt_val = math.sqrt(64)     # 8.0 (Square root)


# 4. EXPONENTIAL & LOGARITHMIC FUNCTIONS (Common)
# Powers, exponents, and logs used in data analysis and algorithms.
exp_val = math.exp(2)        # e raised to the power of 2
natural_log = math.log(10)   # Natural logarithm (base e)
log_base_10 = math.log10(100)# 2.0 (Logarithm base 10)


# 5. TRIGONOMETRIC FUNCTIONS (Less Common)
# Used in graphics, game dev, and physics calculations (inputs are in radians).
angle_rad = math.radians(90) # Converts degrees to radians (pi / 2)
sin_val = math.sin(angle_rad)# 1.0
cos_val = math.cos(angle_rad)# 0.0 (approx)
tan_val = math.tan(angle_rad)# Infinity (approx)


# 6. ADVANCED & SPECIALIZED MATH FUNCTIONS (Least Common)
# Specialized functions for complex engineering, statistics, or floating-point precision.
hypotenuse = math.hypot(3, 4)        # 5.0 (Calculates Euclidean distance / hypotenuse)
gcd_val = math.gcd(24, 36)           # 12 (Greatest Common Divisor)
is_finite = math.isfinite(100.5)     # True (Checks if number is a finite number)
is_nan = math.isnan(float('nan'))    # True (Checks if value is Not a Number)