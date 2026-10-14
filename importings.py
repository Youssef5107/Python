# =====================================================
# PYTHON IMPORTS & MODULES COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: BASIC MODULE & SPECIFIC IMPORTS (Most Common)
# =====================================================

# 1. IMPORTING ENTIRE MODULES
# Imports the whole module into your namespace. You must access attributes/functions via dot notation.
import math
import os

print(math.sqrt(16))     # 4.0
print(os.getcwd())       # Prints current working directory


# 2. IMPORTING SPECIFIC FUNCTIONS, CLASSES, OR VARIABLES
# Directly imports specific names into your script's namespace so you don't need dot notation.
from math import sqrt, pi
from datetime import datetime

print(sqrt(25))          # 5.0
print(pi)                # 3.141592653589793
print(datetime.now())    # Prints current timestamp


# =====================================================
# PART 2: ALIASING IMPORTS (Very Common)
# =====================================================

# 1. RENAMING MODULES OR ITEMS WITH `as`
# Useful for shortening long module names or avoiding naming collisions.
import math as m
from datetime import datetime as dt

print(m.factorial(5))    # 120
print(dt.today())        # Prints today's date


# =====================================================
# PART 3: IMPORTING EVERYTHING & STANDARD VS THIRD-PARTY (Common)
# =====================================================

# 1. WILD_CARD IMPORTS (`from module import *`)
# Imports all public names from a module. 
# Best Practice Warning: Generally discouraged in professional code because it clutters 
# the namespace and makes it hard to track where variables/functions originate.
from math import *
print(sin(0))            # Works, but use with caution!


# 2. STANDARD LIBRARY VS THIRD-PARTY VS LOCAL IMPORTS
# Standard Python convention orders imports in three blocks separated by blank lines:
#   1. Standard Library imports (e.g., sys, os, math)
#   2. Third-party packages (e.g., requests, numpy, fastapi)
#   3. Local application/module imports (e.g., from .utils import helper)

import sys               # Standard library
# import requests        # Third-party (uncomment if installed)
# from models import User # Local application module


# =====================================================
# PART 4: RELATIVE & PACKAGE IMPORTS (Less Common / Advanced)
# =====================================================

# When building multi-directory packages, you use relative imports within package structures:
# Assume directory structure:
# my_package/
#   ├── __init__.py
#   ├── core.py
#   └── utils.py

# Inside `core.py`, you can import from a sibling module using a dot:
# from .utils import helper_function

# To import from a parent directory:
# from ..config import settings


# =====================================================
# PART 5: DYNAMIC IMPORTS & sys.path MODIFICATION (Least Common / Advanced)
# =====================================================

# 1. DYNAMIC IMPORTS USING `importlib`
# Importing modules programmatically at runtime using string names.
import importlib

math_module = importlib.import_module("math")
print(math_module.sqrt(9))  # 3.0


# 2. MODIFYING `sys.path` TO LOAD MODULES FROM CUSTOM DIRECTORIES
# Python looks through `sys.path` to find modules. You can append custom paths dynamically.
import sys

# Adding a custom path to the module search list
sys.path.append("/path/to/my/custom_modules")
# import my_custom_module