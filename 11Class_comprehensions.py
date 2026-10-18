'''
Comprehensions in Python provide a concise, readable syntax 
for creating new collections (lists, dictionaries, sets, or generator expressions) 
from existing iterables by combining looping and filtering in a single line.

Where they are used?
Comprehensions are used wherever data needs to be cleaned, transformed, filtered, or reshaped before being consumed.

What are the Types of Comprehensions?
1. List
2. Dictionary
3. Set
4. Generator

List Comprehensions
List comprehensions build and return a new list.

Basic syntax: [expression for item in iterable]

With filtering: [expression for item in iterable if condition]

With if-else transformation: [val_if_true if condition else val_if_false for item in iterable]
'''
menu = ["Plain Dosa", "Idly", "Vada", "Butter Dosa", "Podi Dosa", "Masala Dosa"]

dosa_only = [item for item in menu if "Dosa" in item] # the expression and inside for loop and in if condtion for which we are looking for condition all should be same name. 

print(f"{dosa_only}") # ['Plain Dosa', 'Butter Dosa', 'Podi Dosa', 'Masala Dosa']

'''
Set Comprehensions
Set comprehensions use {} brackets (without key-value colons) and automatically deduplicate values.

Syntax: {expression for item in iterable if condition}
'''
shapes = ["rect",  "pentogon", "hexogon", "poly", "square", "triangle", "circle", "cylinder", "poly", "square", "triangle", "pentogon", "hexogon" ]

uniqe_shape = {unique for unique in shapes} # inside for loop and the expression should be same eg: unique 
print(f"{uniqe_shape}") # {'pentogon', 'triangle', 'poly', 'hexogon', 'cylinder', 'circle', 'rect', 'square'}


# dictionary
recipies = {
    "masala_chai": ["ginger", "cadimom", "clove"],
    "spicy_chai": ["ginger", "clove", "cinnomon", "black pepper"],
    "elachi_chai":["elachi", "ginger", "jaggery"]
}

# complex in set comprehensions 
unique_spices = {spices for incredients in recipies.values() for spices in incredients} # always write final variable in the expression here spices is last variable that stores the final values

print(f"{unique_spices}") # {'clove', 'black pepper', 'elachi', 'cadimom', 'cinnomon', 'jaggery', 'ginger'}

'''
Dictionary Comprehensions
Dictionary comprehensions construct a dict using key-value pairs separated by a colon.

Syntax: {key_expr: value_expr for item in iterable if condition}
'''
biryani_prices = {
    "chicken_biryani":120,
    "Mutton_biryani":250,
    "lolipop_biryani":180,
    "egg_biryani":80
}

discount_biryani_prices = {biryani:price -20 for biryani, price in biryani_prices.items()}
print(f"{discount_biryani_prices}") # {'chicken_biryani': 100, 'Mutton_biryani': 230, 'lolipop_biryani': 160, 'egg_biryani': 60}

'''
Generator Expressions
Using parentheses () instead of brackets creates a generator object rather than building the entire collection in memory at once. 
Values are yielded lazily on demand.

Syntax: (expression for item in iterable if condition)
Generators are mainly to used to reduce the memory size
'''

daily_sales_for_week = [10, 8, 30, 40, 12, 70, 90]

total_in_lakhs = sum(sale for sale in daily_sales_for_week )
print(f"Total sales for this week is {total_in_lakhs}") #Total sales for this week is 260