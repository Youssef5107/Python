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
# PART 2: LIST MUTATION METHODS (APPEND, POP, INSERT, ETC.)
# =====================================================

# 1. APPEND (Most Common)
# Adds an element to the very end of the list (JS equivalent: arr.push).
numbers.append(6)
print(numbers)         # [1, 2, 3, 4, 5, 6]


# 2. POP (Very Common)
# Removes and returns an element at a given index (defaults to the last item).
# JS equivalent: arr.pop()
last_item = numbers.pop()       # Removes 6
first_item = numbers.pop(0)     # Removes element at index 0 (1)
print(numbers)         # [2, 3, 4, 5]


# 3. INSERT (Very Common)
# Inserts an element at a specific index without overwriting.
# JS equivalent: arr.splice(index, 0, item)
numbers.insert(0, 10)  # Inserts 10 at the beginning
print(numbers)         # [10, 2, 3, 4, 5]


# 4. EXTEND (Very Common)
# Appends multiple elements from another iterable to the end of the list.
# JS equivalent: arr.concat(otherArr)
numbers.extend([6, 7])
print(numbers)         # [10, 2, 3, 4, 5, 6, 7]


# 5. REMOVE & CLEAR (Common)
# Removes the *first occurrence* of a specific value.
numbers.remove(10)     # Removes the number 10
print(numbers)         # [2, 3, 4, 5, 6, 7]

# numbers.clear()      # Clears all elements from the list entirely ([]), uncomment to test


# 6. SORTING & REVERSING (Very Common)
# Modifies the list in-place.
scores_list = [45, 12, 89, 33]
scores_list.sort()             # Sorts ascending: [12, 33, 45, 89]
scores_list.sort(reverse=True) # Sorts descending: [89, 45, 33, 12]
scores_list.reverse()          # Reverses current order in-place


# =====================================================
# PART 3: LIST COMPREHENSIONS (The Pythonic Way to Map & Filter)
# =====================================================

# In JavaScript, you might use `arr.map().filter()`. 
# In Python, List Comprehensions are the preferred, most idiomatic equivalent.

# 1. MAPPING EQUIVALENT (Transforming items)
# JS: numbers.map(n => n * 2)
doubled = [n * 2 for n in numbers]
print(doubled)         # [2, 4, 6, 8, 10, 12, 14]


# 2. FILTERING EQUIVALENT (Conditionally selecting items)
# JS: numbers.filter(n => n % 2 == 0)
evens = [n for n in numbers if n % 2 == 0]
print(evens)           # [2, 4, 6]


# 3. COMBINED MAP & FILTER
# JS: numbers.filter(n => n > 2).map(n => n * 10)
filtered_mapped = [n * 10 for n in numbers if n > 2]
print(filtered_mapped) # [30, 40, 50, 60, 70]


# =====================================================
# PART 4: HIGHER-ORDER FUNCTIONS (map, filter, reduce)
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
# PART 5: OTHER USEFUL HIGHER-ORDER UTILITIES (any, all, sorted)
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