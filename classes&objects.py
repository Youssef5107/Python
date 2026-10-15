# =====================================================
# PYTHON CLASSES & OBJECTS (OOP) COMPREHENSIVE REFERENCE
# Ordered from Most Common to Least Common
# =====================================================


# =====================================================
# PART 1: DEFINING CLASSES & INSTANTIATION (Most Common)
# =====================================================

# 1. BASIC CLASS DEFINITION & CONSTRUCTOR (__init__)
# A class is a blueprint for creating objects. `self` refers to the specific instance being created.
class User:
    # The constructor method initializes instance attributes
    def __init__(self, username, email):
        self.username = username  # Instance attribute
        self.email = email        # Instance attribute
        self.is_active = True     # Default attribute value


# 2. INSTANTIATING OBJECTS
# Creating individual objects (instances) from the class blueprint.
user1 = User("youssef5107", "youssef@example.com")
user2 = User("alice123", "alice@example.com")

print(user1.username)    # "youssef5107"
print(user2.email)       # "alice@example.com"


# =====================================================
# PART 2: INSTANCE METHODS & __str__ (Very Common)
# =====================================================

class SecurityProfile:
    def __init__(self, username, clearance_level):
        self.username = username
        self.clearance_level = clearance_level

    # 1. INSTANCE METHOD
    # Functions defined inside a class that operate on instance data via `self`.
    def get_details(self):
        return f"User: {self.username} | Clearance: Level {self.clearance_level}"

    # 2. STRING REPRESENTATION METHOD (__str__)
    # Controls what is returned when print() is called on the object.
    def __str__(self):
        return f"SecurityProfile({self.username})"

# Usage
profile = SecurityProfile("Youssef", 5)
print(profile.get_details())  # "User: Youssef | Clearance: Level 5"
print(profile)                # "SecurityProfile(Youssef)"


# =====================================================
# PART 3: INHERITANCE (Common)
# =====================================================

# 1. BASE (PARENT) CLASS
class Device:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.is_online = True

    def ping(self):
        return f"Pinging {self.ip_address}..."


# 2. DERIVED (CHILD) CLASS
# Inherits attributes and methods from `Device`, and can extend or override them.
class Router(Device):
    def __init__(self, ip_address, brand):
        super().__init__(ip_address)  # Calls parent constructor
        self.brand = brand

    # Overriding a method from the parent class
    def ping(self):
        base_msg = super().ping()
        return f"{base_msg} [Router Brand: {self.brand}]"

# Usage
my_router = Router("192.168.1.1", "Cisco")
print(my_router.ping())       # "Pinging 192.168.1.1... [Router Brand: Cisco]"


# =====================================================
# PART 4: ENCAPSULATION & ACCESS MODIFIERS (Common)
# =====================================================

# Python uses naming conventions to signal privacy:
# - Public: `variable` (accessible anywhere)
# - Protected: `_variable` (internal use warning, single underscore)
# - Private: `__variable` (name-mangled, restricted access)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (Name mangled to _BankAccount__balance)

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance

    # Setter method to safely modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

account = BankAccount("Youssef", 1000)
account.deposit(500)
print(account.get_balance())        # 1500
# print(account.__balance)          # AttributeError! Cannot access directly.


# =====================================================
# PART 5: CLASS METHODS & STATIC METHODS (Less Common / Advanced)
# =====================================================

class NetworkConfig:
    DEFAULT_PORT = 80

    def __init__(self, port):
        self.port = port

    # 1. CLASS METHOD (@classmethod)
    # Operates on the class itself rather than instances (receives `cls` instead of `self`).
    @classmethod
    def set_default_port(cls, new_port):
        cls.DEFAULT_PORT = new_port

    # 2. STATIC METHOD (@staticmethod)
    # Utility function that doesn't access or modify class or instance state (takes no `self` or `cls`).
    @staticmethod
    def is_valid_port(port):
        return 1 <= port <= 65535

# Usage
print(NetworkConfig.is_valid_port(8080))  # True
NetworkConfig.set_default_port(443)
print(NetworkConfig.DEFAULT_PORT)         # 443