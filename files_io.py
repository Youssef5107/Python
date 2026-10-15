# =====================================================
# PYTHON FILE I/O (READING & WRITING) COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: CONTEXT MANAGERS & BASIC WRITING (Most Common)
# =====================================================

# 1. USING THE `with` STATEMENT (Context Manager)
# Best Practice: Always use `with` when handling files. It automatically closes the file 
# safely, even if an exception occurs during reading or writing.

# Writing to a file (Mode 'w' creates the file or overwrites it entirely if it exists)
with open("notes.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file I/O is powerful.\n")


# 2. APPENDING TO A FILE (Mode 'a')
# Appends data to the end of the file without wiping existing content.
with open("notes.txt", "a") as file:
    file.write("Appending this new security log line.\n")


# =====================================================
# PART 2: READING TEXT FILES (Most Common)
# =====================================================

# 1. READING THE ENTIRE FILE AT ONCE (`.read()`)
# Loads the entire file content into a single string. (Use caution with huge files).
with open("notes.txt", "r") as file:
    content = file.read()
    print("--- Full Content ---")
    print(content)


# 2. READING LINE-BY-LINE ITERATION (Memory Efficient)
# Iterating directly over the file object is the most Pythonic and memory-efficient 
# way to process large text or log files line by line.
with open("notes.txt", "r") as file:
    print("--- Line by Line ---")
    for line in file:
        print(line.strip())  # .strip() removes trailing newline characters


# 3. READING LINES INTO A LIST (`.readlines()`)
# Reads all lines and stores them as elements in a list.
with open("notes.txt", "r") as file:
    lines_list = file.readlines()
    print(lines_list)       # ['Hello, World!\n', 'Python file I/O is powerful.\n', ...]


# =====================================================
# PART 3: FILE MODES REFERENCE (Very Common)
# =====================================================

# Summary of standard file opening modes:
#   'r'  - Read (default mode). Raises FileNotFoundError if the file doesn't exist.
#   'w'  - Write. Creates a new file or truncates/overwrites an existing file.
#   'a'  - Append. Creates a new file or adds data to the end of an existing file.
#   'r+' - Read and Write. Allows both reading and writing (pointer starts at the beginning).
#   'b'  - Binary mode (e.g., 'rb', 'wb'). Used for non-text files like images or binaries.


# =====================================================
# PART 4: WORKING WITH BINARY FILES (Common in Cybersecurity)
# =====================================================

# Reading and writing raw bytes (essential for handling executables, network packets, or images).
binary_data = b"\x41\x42\x43\x44"  # ASCII bytes for A, B, C, D

# Write binary data
with open("binary_payload.bin", "wb") as bin_file:
    bin_file.write(binary_data)

# Read binary data back
with open("binary_payload.bin", "rb") as bin_file:
    read_bytes = bin_file.read()
    print(read_bytes)       # b'ABCD'


# =====================================================
# PART 5: FILE SYSTEM UTILITIES WITH `pathlib` (Modern & Clean)
# =====================================================

# Python's modern standard library for handling file paths and checks (`pathlib`).
from pathlib import Path

file_path = Path("notes.txt")

# 1. Check if a file exists
if file_path.exists():
    print(f"'{file_path.name}' exists and is {file_path.stat().st_size} bytes.")

# 2. Reading text quickly using pathlib (Python 3.9+)
# text_content = file_path.read_text()
# print(text_content)