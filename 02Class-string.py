import sys
'''
core:
String is an immutable object 
Immutable means unchangeable in-place. Once a string object is created in memory,
 its contents can never be modified, added to, or deleted.
 chai = "Masala Chai"

# Trying to change the first letter 'M' to 'G'
chai[0] = "G"
print(f"{chai}")
TypeError: 'str' object does not support item assignment
indexing:
Indexing allows you to pull out a single character using its 0-based position inside square brackets [].
Python supports both positive (left-to-right) and negative (right-to-left) indexing:
String:   P   y   t   h   o   n
 Index:    0   1   2   3   4   5
-Index:   -6  -5  -4  -3  -2  -1
slicing:
Slicing extracts a range of characters. The syntax is:$$\text{string}[\text{start} : \text{stop} : \text{step}]$$start: 
Index where the slice begins (inclusive). Defaults to 0.stop: Index where the slice ends (exclusive — does not include this index). 
Defaults to the end of the string.step: How many indices to advance each time. Defaults to 1.
'''

text = "GingerTea"
#  G  i  n  g  e  r  T  e  a
#  0  1  2  3  4  5  6  7  8

# 1. Basic slice [start:stop]
print(text[0:6])    # 'Ginger' (indices 0 through 5)
print(text[6:9])    # 'Tea'    (indices 6 through 8)

# 2. Omitting start or stop
print(text[:6])     # 'Ginger' (from the beginning up to index 5)
print(text[6:])     # 'Tea'    (from index 6 to the very end)
print(text[:])      # 'GingerTea' (full copy of the string)

# 3. Using step [start:stop:step]
print(text[0:6:2])  # 'Gne' (indices 0, 2, 4)
print(text[::2])    # 'GneTa' (every 2nd character across the whole string)

# 4. Slicing with negative step (Reverse a string)
print(text[::-1])   # 'aeTregniG'

#special charecters encoded and decoded
label_value = "Spéciæl Țea" 
encoded_value = label_value.encode("utf-8")
print(label_value) # Spéciæl Țea
print(encoded_value) # b'Sp\xc3\xa9ci\xc3\xa6l \xc8\x9aea'
decoded_value = encoded_value.decode("utf-8")
print(decoded_value) # Spéciæl Țea
