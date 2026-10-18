import sys
print (sys.version)
"""
Everything in python is an object
and every object have identity, type, value
and objects are both mutalble and immutable
mutable means we can do changes in that object
immutable means its not editable, changes are strictly not allowed in it
and identity of object will helps us to know weather it is changable or not changabled.

"""
# example of immutable data type the id of every value is different 
sugar_amount = 3
print(f"intial sugar: {sugar_amount}")
print(f"id of 1st sugar amount: {id(sugar_amount)}")
sugar_amount = 10
print(f"second sugar amount: {sugar_amount}")
print(f"id of second sugar amount:{id(sugar_amount)}")

# for every object value there is ID 
"""
id of 1st sugar amount: 4329362640
id of second sugar amount:4329362864
"""

# example of mutable the id will be same the values will get change to that id 
spice_amount = set()
spice_amount.add(4)
print(f"spice amount of 4 value id: {id(spice_amount)}")
print(f"spice amount: {spice_amount}")
spice_amount.add(12)
print(f"spice amount of 12 value id: {id(spice_amount)}")
print(f"spice amount: {spice_amount}")
#float example
print(f"{95.5-95.499999999999}") # 9.947598300641403e-13
print(f"float Info:{sys.float_info}")
''' 
float Info:sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
 min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, 
 epsilon=2.220446049250313e-16, radix=2, rounds=1)
'''

'''
spice amount of 4 value id: 4562765408
spice amount: {4}
spice amount of 12 value id: 4562765408
spice amount: {4, 12}
'''

"""
In python we have differnt types of numbers
integers
booleans
real numbers or floting numbers
complex numbers (example: 2+3j like that iot numbers)
"""
tea_powder_grams = 7
ginger_grams=4
total_grams = tea_powder_grams + ginger_grams
no_of_cups = 9
total_sugar_cubes = 9
no_people = 7
people_said_no = 2
total_drinking_people = no_people -people_said_no
base_flavour = 2
scale_flavour_strength = 3
how_many_tea_leaves_harvested_this_year= 1_000_000_000


# single / gives floting value
sugar_cube_per_cup = total_sugar_cubes / total_drinking_people
# double // divder gives you integer
cups_per_person = no_of_cups // total_drinking_people
# modulo % to see the reminder
remaining_cups = no_of_cups % total_drinking_people
# eponential ** this will do a*a*a...
powerful_flavaour = base_flavour ** scale_flavour_strength

print(f"total grams :{total_grams}")
print(f"sugar cube per cup  :{sugar_cube_per_cup}")
print(f"cups per person :{cups_per_person}")
print(f"Remaining cups: {remaining_cups}")
print(f"powerful flavour: {powerful_flavaour}")
print(f"Tea leaves harvested this year: {how_many_tea_leaves_harvested_this_year}")
"""
total grams :11
sugar cube per cup  :1.8
cups per person :1
Remaining cups: 4
powerful flavour: 8 -- 2*2*2
Tea leaves harvested this year: 1000000000
"""