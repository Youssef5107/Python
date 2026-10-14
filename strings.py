# ==========================================
# PYTHON STRINGS COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# ==========================================


# 1. STRING CREATION & BASIC ASSIGNMENT (Most Common)
# Storing text data in variables using single, double, or triple quotes.
single_quote = 'Hello, World!'
double_quote = "Python Development"
multi_line = """This is a multi-line
string used for blocks of text."""


# 2. STRING CONCATENATION & f-STRINGS (Most Common)
# Combining or formatting variables inside strings. f-strings are the modern standard.
first_name = "Youssef"
last_name = "Ahmed"
full_name = f"{first_name} {last_name}"  # f-string (Recommended)
combined_str = "Hello " + first_name    # Traditional concatenation


# 3. CHANGING CASE (Very Common)
# Converting text formats for validation, UI display, or normalization.
text = "python programming"
upper_text = text.upper()          # "PYTHON PROGRAMMING"
lower_text = text.lower()          # "python programming"
title_text = text.title()          # "Python Programming" (Capitalizes each word)
capitalize_text = text.capitalize() # "Python programming" (Capitalizes first letter)


# 4. FINDING SUBSTRINGS & COUNTING (Very Common)
# Checking if text exists or locating its position.
sentence = "Learn Python for network scripting and web development."
contains_python = "Python" in sentence     # Returns True / False
position = sentence.find("network")        # Returns index number (or -1 if not found)
count_e = sentence.lower().count("e")      # Counts how many times 'e' appears


# 5. STRIPPING WHITESPACE (Very Common)
# Cleaning up accidental extra spaces, tabs, or newlines from user input or files.
messy_string = "   admin@local   \n"
clean_string = messy_string.strip()       # Removes spaces from both ends
left_clean = messy_string.lstrip()        # Removes left-side spaces
right_clean = messy_string.rstrip()       # Removes right-side spaces


# 6. SPLITTING & JOINING STRINGS (Very Common)
# Converting strings into lists and lists back into strings (essential for parsing command outputs!).
csv_data = "192.168.1.1,admin,active"
ip_list = csv_data.split(",")             # Splits into a list: ['192.168.1.1', 'admin', 'active']

reconstructed_str = " - ".join(ip_list)   # Joins list back with a separator: "192.168.1.1 - admin - active"


# 7. REPLACING TEXT (Common)
# Swapping specific words, characters, or symbols inside a string.
log_entry = "STATUS: ERROR - Connection failed"
fixed_log = log_entry.replace("ERROR", "SUCCESS")  # "STATUS: SUCCESS - Connection failed"


# 8. CHECKING STRING CONTENT / START / END (Common)
# Validation checks (useful in automation and scripts).
filename = "ipsweep.sh"
is_script = filename.endswith(".sh")       # Returns True
is_doc = filename.startswith("doc")        # Returns False
is_alpha = "Python".isalpha()              # True (only letters)
is_digit = "12345".isdigit()               # True (only numbers)


# 9. STRING SLICING (Moderately Common)
# Extracting specific portions of a string using indexes [start:end:step].
target_ip = "192.168.1.50"
prefix = target_ip[0:7]                    # Extracts "192.168"
last_octet = target_ip[-2:]                # Extracts "50" (using negative indexing from the end)
reversed_str = target_ip[::-1]             # Reverses the string


# 10. ALIGNMENT, PADDING & CENTER (Less Common)
# Formatting string text width for console printouts or tables.
title = "SCAN RESULTS"
padded_left = title.ljust(20, "-")         # "SCAN RESULTS--------"
padded_right = title.rjust(20, "-")        # "--------SCAN RESULTS"
centered = title.center(20, "=")           # "====SCAN RESULTS===="


# 11. ENCODING & DECODING (Least Common / Advanced)
# Converting standard strings into byte objects for network sockets or cryptographic hashes.
raw_text = "SecretPayload"
byte_data = raw_text.encode("utf-8")       # Converts to bytes: b'SecretPayload'
back_to_str = byte_data.decode("utf-8")    # Converts back to string