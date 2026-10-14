# =====================================================
# PYTHON ARRAYS (LISTS) & HIGHER-ORDER FUNCTIONS REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: LIST CREATION & BASIC OPERATIONS (Most Common)
# =====================================================

# 1. CREATING LISTS & INDEXING
# Lists are ordered, mutable collections that can hold mixed data types.
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

print(numbers[0])      # 1 (First item via zero-based index)
print(numbers[-1])     # 5 (Last item via negative indexing)


# 2. SLICING LISTS
# Extracting sub-segments using [start:end:step].
print(numbers[1:4])    # [2, 3, 4] (Items from index 1 up to 4)
print(numbers[:3])     # [1, 2, 3] (From beginning to index 3)
print(numbers[::2])    # [1, 3, 5] (Every second item / step of 2)


# =====================================================
# PART 2: LIST COMPREHENSIONS (The Pythonic Way to Map & Filter)
# =====================================================

# In JavaScript, you might use `arr.map().filter()`. 
# In Python, List Comprehensions are the preferred, most idiomatic equivalent.

# 1. MAPPING EQUIVALENT (Transforming items)
# JS: numbers.map(n => n * 2)
doubled = [n * 2 for n in numbers]
print(doubled)         # [2, 4, 6, 8, 10]


# 2. FILTERING EQUIVALENT (Conditionally selecting items)
# JS: numbers.filter(n => n % 2 == 0)
evens = [n for n in numbers if n % 2 == 0]
print(evens)           # [2, 4]


# 3. COMBINED MAP & FILTER
# JS: numbers.filter(n => n > 2).map(n => n * 10)
filtered_mapped = [n * 10 for n in numbers if n > 2]
print(filtered_mapped) # [30, 40, 50]


# =====================================================
# PART 3: HIGHER-ORDER FUNCTIONS (map, filter, reduce)
# =====================================================

# Python supports functional programming style via built-in functions.
# Note: These return iterator objects in Python 3, so wrap them in `list()` to view.

# 1. MAP (Equivalent to JS Array.prototype.map)
# Applies a function to every item in an iterable.
nums = [1, 2, 3, 4]
squared_map = list(map(lambda x: x ** 2, nums))
print(squared_map)     # [1, 4, 9, 16]


# 2. FILTER (Equivalent to JS Array.prototype.filter)
# Filters elements based on a boolean-returning function.
evens_filter = list(filter(lambda x: x % 2 == 0, nums))
print(evens_filter)    # [2, 4]


# 3. REDUCE (Equivalent to JS Array.prototype.reduce)
# Rolls through elements to accumulate a single value (requires importing from functools).
from functools import reduce

sum_reduce = reduce(lambda acc, x: acc + x, nums, 0)
print(sum_reduce)      # 10 (Accumulates total sum)


# =====================================================
# PART 4: OTHER USEFUL HIGHER-ORDER UTILITIES (any, all, sorted)
# =====================================================

# 1. ANY & ALL (Short-circuit evaluation over iterables)
scores = [85, 90, 78, 92]
print(any(s > 90 for s in scores))   # True (At least one item satisfies condition)
print(all(s >= 70 for s in scores))  # True (All items satisfy condition)


# 2. SORTED WITH CUSTOM KEYS (Equivalent to JS arr.sort((a,b) => ...))
words = ["banana", "apple", "cherry"]
# Sort by string length using a lambda key function
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)              # ['apple', 'banana', 'cherry']