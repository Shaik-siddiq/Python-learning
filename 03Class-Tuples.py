'''
A tuple is an ordered, immutable collection of items in Python.
While lists use square brackets [] and can be changed, tuples use parentheses () 
(or just comma separation) and cannot be modified after creation.
'''
spices = ("cardamom", "ginger", "clove")
coordinates = (12.9716, 77.5946)
single_item = ("masala",)  # Note the trailing comma; without it, Python treats it as a plain string
'''
Core Properties of Tuples:Ordered: Elements stay in the exact position you defined.
 Indexing and slicing work identically to strings and lists (spices[0] $\rightarrow$ "cardamom").
 Immutable: You cannot append, remove, or reassign elements.
'''
# spices[0] = "cinnamon"  # Raises TypeError: 'tuple' object does not support item assignment

'''
Heterogeneous: A single tuple can store mixed data types (("Chai", 2, True, 15.5)).

Hashable (Usable as Dict Keys): Because they are immutable, tuples containing only immutable items 
can be used as dictionary keys or stored in sets, which lists cannot do.
'''
'''
Tuple Unpacking
A powerful tuple feature is unpacking items directly into distinct variables:
'''
dimensions = (1920, 1080)
width, height = dimensions

print(width)   # 1920
print(height)  # 1080

'''
What is Membership Testing?
Membership testing checks whether a specific value exists inside a collection (such as a tuple, list, string, set, or dictionary).

Python uses two operators for this:

in: Returns True if the item is present, otherwise False.

not in: Returns True if the item is not present, otherwise False.
'''
ingredients = ("tea leaves", "milk", "sugar", "ginger")

# Checking with 'in'
has_milk = "milk" in ingredients
print(has_milk)  # True

has_coffee = "coffee" in ingredients
print(has_coffee)  # False

# Checking with 'not in'
is_vegan = "milk" not in ingredients
print(is_vegan)  # False (because milk is present)

selected_spice = "cinnamon"
allowed_spices = ("cardamom", "ginger", "clove", "cinnamon")

if selected_spice in allowed_spices:
    print(f"Adding {selected_spice} to the pot.")
else:
    print("Spice not found in recipe.")

'''
Takeaway: For small collections (like a dozen recipe ingredients),
 membership testing on a tuple is very fast. 
 If you need to test membership across thousands or millions of elements frequently,
convert the collection to a set first for much faster lookups.
'''
subjects = ("maths", "science", "social")
(sub1, sub2, sub3) = subjects
print(sub1, sub3) # maths social

maths_students, science_students, social_students = 23, 31, 9
print(science_students) # 31
science_students, maths_students = 23, 31
no_of_subjects = ("maths, social, science")
print(f"swaping of values : {science_students, maths_students}") # swaping of values : (23, 31)
print(f"is english present in no of subjects: {"english" in no_of_subjects }") # is english present in no of subjects: False
# Tuple is case sensitive. 
print(f"Maths is no of subjects: {"Maths" in no_of_subjects}") # Maths is no of subjects: False