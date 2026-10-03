'''
A dictionary (dict) in Python is an unordered (or insertion-ordered), mutable collection of data stored as key-value pairs.

Instead of accessing elements by a numeric index (like list[0]), you access them by a unique descriptive key (like user["name"]).
'''
# A simple dictionary
chai_recipe = {
    "tea_powder_grams": 7,
    "ginger_grams": 4,
    "milk_ml": 100,
    "water_ml": 150
}

print(chai_recipe["ginger_grams"])  # Output: 4

'''
Key Rules for Dictionaries

Keys must be unique: A dictionary cannot have duplicate keys. If you assign a value to an existing key, it overwrites the old value.
Keys must be immutable (hashable): You can use strings, numbers, or tuples as keys. You cannot use lists, sets, or other dictionaries as keys.
Values can be anything: Values can be any data type—integers, strings, lists, sets, or even other nested dictionaries.
Insertion-ordered: Since Python 3.7+, dictionaries preserve the order in which items are added.
'''

user = {"id": 101, "name": "Siddiq", "role": "developer"}

# Direct bracket access (raises KeyError if key is missing)
print(user["name"])  # 'Siddiq'

# Safe access with .get() (returns None or a default value instead of crashing)
print(user.get("email"))          # None
print(user.get("email", "N/A"))   # 'N/A'

# Add a new key-value pair
user["email"] = "dev@example.com"

# Update an existing key
user["role"] = "lead_developer"

# Update multiple values at once
user.update({"status": "active", "login_count": 5})
# .pop() removes the key and returns its value
role = user.pop("role")

# del statement removes without returning
del user["status"]
'''
3. Iterating Over Dictionaries
You can loop through keys, values, or both simultaneously:
'''
stock = {"tea": 40, "coffee": 25, "sugar": 15}

# 1. Loop through keys (default)
for item in stock:
    print(item)  # 'tea', 'coffee', 'sugar'

# 2. Loop through values
for count in stock.values():
    print(count)  # 40, 25, 15

# 3. Loop through both (key, value) using .items() — most common
for item, count in stock.items():
    print(f"{item}: {count} units")
'''
4. Membership Testing (in)
In dictionaries, the in operator checks keys, not values:
'''
user = {"name": "Siddiq", "active": True}

print("name" in user)     # True (checks keys)
print("Siddiq" in user)   # False (does NOT check values)

# To check values explicitly:
print("Siddiq" in user.values())  # True

'''
 Why Dictionaries Are So Fast (O(1))Under the hood, 
 Python dictionaries are implemented as hash tables:
 When you look up a key (e.g., user["id"]), Python hashes the key using an internal hash function to calculate its exact memory bucket.
 It does not scan through items one by one like a list does (O(n)).
 Key lookup, insertion, and deletion all happen in constant time (O(1)),
   making them the standard data structure for fast lookups, caches, JSON payloads, and entity modeling in Python.
'''

'''
The difference between an object and a dictionary depends on whether you are looking at Python specifically or comparing Python to languages like JavaScript:

In Python: A dictionary is just one specific type of object, while custom objects (instances of classes) are designed to bundle both data and behavior.

Python vs. JavaScript: A Python dictionary is a pure key-value hash map, whereas a JavaScript object doubles as both a dictionary-like hash map and an OOP class instance.

1. In Python: Object vs. Dictionary
In Python, "everything is an object"—integers, functions, strings, lists, and dictionaries are all objects under the hood.

However, when developers contrast an object (a class instance) with a dictionary, they mean:
'''

# A DICTIONARY: Raw data container (Key-Value map)
user_dict = {
    "name": "Siddiq",
    "role": "developer"
}

# Access via brackets/keys:
print(user_dict["name"])

# A CUSTOM OBJECT: Data + Behavior (Class instance)
class User:
    def __init__(self, name: str, role: str):
        self.name = name        # Attribute (Data)
        self.role = role

    def promote(self):         # Method (Behavior)
        self.role = f"Senior {self.role}"

user_obj = User("Siddiq", "developer")

# Access via dot notation and call methods:
print(user_obj.name)
user_obj.promote()
print(user_obj.role)  # 'Senior developer'

"""
Python Dictionary vs. JavaScript Object
If you are coming from JavaScript, the terminology can be confusing because JS uses {} for both concepts:
In JavaScript:An object { name: "Siddiq", role: "developer" } serves as a generic key-value store, allows dot notation (user.name), and supports prototypes and attached functions.
In Python:A dictionary { "name": "Siddiq" } is strictly a data container. You cannot use dot notation (user_dict.name raises an AttributeError).If you want methods, inheritance, and encapsulation, you define a class.
When to Use Which in Python
Use a Dictionary when:
Parsing or producing JSON APIs.Dealing with dynamic data where keys change at runtime.
You need fast $O(1)$ key lookups, frequency counting, or caching.
Use an Object (Class / Dataclass) when:
You need business logic, validation, or methods that operate on the data.
You want a fixed schema with type safety, code completion, and IDE suggestions.
You want object-oriented features like inheritance or encapsulation.
(Tip: If you just want a structured object with dot-notation and no complex methods, Python provides @dataclass):
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    role: str

user = User(name="Siddiq", role="developer")
print(user.name)  # Clean dot notation, structured like an object