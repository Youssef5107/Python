# =====================================================
# PYTHON TUPLES COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: TUPLE CREATION & BASIC ASSIGNMENT (Most Common)
# =====================================================

# 1. DEFINING TUPLES
# Tuples are ordered, immutable (unchangeable) collections. Defined using parentheses `()`.
coordinates = (10.0, 20.0)
single_item_tuple = (42,)     # Note: Trailing comma is mandatory for single-item tuples!
empty_tuple = ()


# 2. TUPLE PACKING & UNPACKING (Very Common)
# Assigning values into a tuple ("packing") and extracting them back into variables ("unpacking").
person = ("Youssef", 25, "Developer")  # Packing
name, age, role = person               # Unpacking

# Using wildcard unpacking (*) to capture remaining elements
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4] (Captured as a list)
print(last)    # 5


# =====================================================
# PART 2: ACCESSING ELEMENTS & SLICING (Most Common)
# =====================================================

# 1. INDEXING & NEGATIVE INDEXING
# Accessing items via zero-based positions, identical to lists.
colors = ("red", "green", "blue", "yellow")
print(colors[0])       # "red"
print(colors[-1])      # "yellow" (Last item)


# 2. SLICING TUPLES
# Extracting sub-segments using [start:end:step].
print(colors[1:3])     # ('green', 'blue')
print(colors[::-1])    # ('yellow', 'blue', 'green', 'red') (Reversed tuple)


# =====================================================
# PART 3: BUILT-IN METHODS (COUNT & INDEX) (Common)
# =====================================================

# Because tuples are immutable, they do not have mutation methods like `append`, `pop`, or `sort`. 
# They only have two built-in methods:

scores = (90, 85, 90, 78, 92, 90)

# 1. COUNT
# Returns the number of times a specified value occurs in the tuple.
print(scores.count(90))    # 3


# 2. INDEX
# Returns the index of the first occurrence of a specified value.
print(scores.index(78))    # 3


# =====================================================
# PART 4: IMMUTABILITY & WHY USE TUPLES? (Conceptual)
# =====================================================

# 1. ATTEMPTING MUTATION RAISES AN ERROR
# tuples cannot be modified after creation. The following line raises a TypeError:
# colors[0] = "purple"   # Error: 'tuple' object does not support item assignment


# 2. WHY USE TUPLES OVER LISTS?
# - Data Integrity: Protects fixed data from accidental modification.
# - Performance: Tuples consume less memory and are faster to initialize than lists.
# - Dictionary Keys: Because they are immutable (hashable), tuples can be used as dictionary keys 
#   (lists cannot).
location_data = {
    (30.0444, 31.2357): "Cairo Office",
    (40.7128, -74.0060): "New York Office"
}
print(location_data[(30.0444, 31.2357)])  # "Cairo Office"