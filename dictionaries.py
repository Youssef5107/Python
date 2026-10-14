# =====================================================
# PYTHON DICTIONARIES COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: DICTIONARY CREATION & BASIC ACCESS (Most Common)
# =====================================================

# 1. DEFINING DICTIONARIES
# Dictionaries store key-value pairs. Keys must be immutable (strings, numbers, tuples).
user = {
    "name": "Youssef",
    "age": 25,
    "is_active": True,
    "roles": ["developer", "admin"]
}

# Alternative constructor using `dict()`
settings = dict(theme="dark", notifications=True)


# 2. ACCESSING VALUES (Bracket Notation vs .get())
# Bracket notation raises a KeyError if the key doesn't exist.
print(user["name"])          # "Youssef"
# print(user["email"])       # KeyError!

# Using .get() safely returns `None` (or a custom default) if the key is missing.
print(user.get("email"))                 # None
print(user.get("email", "N/A"))          # "N/A" (Custom default)


# =====================================================
# PART 2: ADDING, UPDATING, & REMOVING DATA (Very Common)
# =====================================================

# 1. ADDING & UPDATING KEY-VALUE PAIRS
user["email"] = "youssef@example.com"    # Adds new key-value pair
user["age"] = 26                         # Updates existing key value

# Using .update() to merge multiple keys at once
user.update({"status": "Online", "level": "Senior"})


# 2. SETDEFAULT (Adding with a fallback if key doesn't exist)
# Returns current value if key exists; otherwise, sets it to the default value.
user.setdefault("country", "Egypt")      # Sets "country": "Egypt" because it didn't exist


# 3. REMOVING ITEMS
# pop() removes a specific key and returns its value
role = user.pop("is_active", None)       # Removes "is_active" safely

# popitem() removes and returns the *last inserted* (key, value) pair as a tuple (Python 3.7+)
last_pair = user.popitem()

# del keyword removes a key by reference
del user["roles"]


# =====================================================
# PART 3: DICTIONARY VIEWS: KEYS, VALUES, & ITEMS (Very Common)
# =====================================================

# Iterating over dictionary views dynamically reflecting changes.
profile = {"username": "youssef5107", "repo_count": 10, "public": True}

# 1. .keys() - Returns all keys
print(profile.keys())        # dict_keys(['username', 'repo_count', 'public'])

# 2. .values() - Returns all values
print(profile.values())      # dict_values(['youssef5107', 10, True])

# 3. .items() - Returns key-value pairs as tuples (Essential for loops!)
for key, value in profile.items():
    print(f"{key}: {value}")


# =====================================================
# PART 4: ADVANCED DICTIONARY OPERATIONS (Common)
# =====================================================

# 1. DICTIONARY COMPREHENSIONS (The Pythonic Way to Transform Dictionaries)
# Creating dictionaries on the fly from iterables.
numbers = [1, 2, 3, 4]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)          # {1: 1, 2: 4, 3: 9, 4: 16}


# 2. MERGING DICTIONARIES USING THE UNION OPERATOR (|) (Python 3.9+)
# Combining two dictionaries cleanly.
defaults = {"theme": "light", "timeout": 30}
user_prefs = {"theme": "dark"}

merged_settings = defaults | user_prefs
print(merged_settings)       # {'theme': 'dark', 'timeout': 30} (user_prefs overrides defaults)


# 3. CHECKING IF KEYS EXIST
# Using the `in` operator (extremely fast O(1) time complexity for dictionaries).
if "username" in profile:
    print("Username key exists!")