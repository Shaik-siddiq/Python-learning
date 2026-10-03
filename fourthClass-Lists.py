'''
Traditional array and a Python list are fundamentally different data structures under the hood, even though both store sequences of items.

Here is why Python calls them lists instead of arrays.

1. Heterogeneous vs. Homogeneous Data
Traditional Array: A true array requires every single element to be of the exact same data type (e.g., an array strictly of 32-bit integers or 64-bit floats).

Python List: A list is heterogeneous. You can mix any data types together inside the same container without any errors:

'''
mixed_list = [42, "chai", 3.14, True, [1, 2], {"sugar": 2}]
'''
2. Contiguous Values vs. Array of References
This is the biggest architectural difference in memory:

In a classic Array (C, C++, Java): The computer reserves a single,
 contiguous block of memory where the raw values themselves sit right next to each other.

Plaintext
Memory Layout for an Integer Array:
[ 10 ] [ 20 ] [ 30 ] [ 40 ]   <-- Actual byte values stored contiguously
In a Python List: Python does not store the raw values in the list. 
Python objects are stored in arbitrary locations in memory (the heap),
 and the list stores a contiguous sequence of pointers (memory addresses / references) pointing to those objects:

Plaintext
Python List:
[ ptr1 | ptr2 | ptr3 ]
   |      |      |
   v      v      v
 "chai"   42    3.14        <-- Objects scattered in memory
Technically, in CPython (standard Python), a list is implemented as a dynamic array of pointers (PyObject**). 
Because it only holds pointers, it behaves like a flexible list rather than a flat, raw-value array.
'''
'''
 3. Fixed Size vs. Dynamic ResizingTraditional Array: Usually has a fixed size declared upfront at creation time (e.g., int arr[5]). 
 If you need a 6th item, you must manually allocate a larger block of memory and copy elements over.Python List: A list is dynamic. 
 It automatically expands and contracts as you call .append(), .extend(), or .pop(). 
 Python manages overallocation behind the scenes so appending is amortized $O(1)$ time.
'''
'''
Does Python Have Real Arrays?
Yes, if you ever need genuine, low-level arrays in Python, they exist through separate modules:

The built-in array module: Stores homogeneous C-style raw values (integers, floats, bytes):

import array
# 'i' means signed integer only
numbers = array.array('i', [1, 2, 3, 4])
NumPy Arrays (ndarray): The standard in data science and AI. 
NumPy allocates contiguous memory blocks for raw numbers and runs fast, vectorised C operations over them.
'''
incredients = ["water", "milk", "coffee", "tea"]
print(incredients) # ['water', 'milk', 'coffee', 'tea']
incredients.append("sugar")
incredients.remove("coffee")
chai_incredients = ["ginger, cardamom"]
chai_incredients.extend(incredients)
print(f"increadients for making tea: {chai_incredients}") # increadients for making tea: ['ginger, cardamom', 'water', 'milk', 'tea', 'sugar']
incredients.append("coffee")
incredients.remove("tea")
print(f"increadients for making coffee: {incredients}") # increadients for making coffee: ['water', 'milk', 'sugar', 'coffee']
print(f"chai incredients check: {chai_incredients}") # chai incredients check: ['ginger, cardamom', 'water', 'milk', 'tea', 'sugar']
make_black_tea = incredients.copy()
make_black_tea.extend(["black tea poweder", "lemon", "honey"])
for item in ["coffee", "milk", "sugar"] : make_black_tea.remove(item)
print(f"black tea incredients:{make_black_tea}") # black tea incredients:['water', 'black tea poweder', 'lemon', 'honey']
sugar_levels = [1,2,3,4,5,6]
print(f"maximum sugar levels:{max(sugar_levels)}") # maximum sugar levels:6
print(f"minimum sugar levels: {min(sugar_levels)}") # minimum sugar levels: 1

# Operator overloading
basic_liquids = ["honey", "water"]
lemon_tea = ["lemon"]
print(f"leam tea all incredtients:{basic_liquids+lemon_tea}") # leam tea all incredtients:['honey', 'water', 'lemon']

strong_black_tea = ["black tea", "water"] * 3
print(f"strong black tea:{strong_black_tea}") # strong black tea:['black tea', 'water', 'black tea', 'water', 'black tea', 'water']
