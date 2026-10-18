'''
A function in Python is a reusable block of organized code designed to perform a single, specific task. 
Functions make programs modular, readable, and maintainable by avoiding repeated logic.
You define a function using the def keyword, followed by the function name, parentheses (), and a colon :. The code inside is indented.
'''
# Functions can accept inputs (parameters) and send data back to the caller using return.
def orderChai(name, chai_type):
    print(f"{name} ordered {chai_type}")

orderChai("sid", "lemon tea")

def summuraize_data():
    print("summarizing Data")
def fetch_salse():
    print("Fetching sales")
def filtering_orders():
    print("Filtering Orders")

def generating_reports():
    fetch_salse()
    filtering_orders()
    summuraize_data()

generating_reports()

def calculate_bill(cups, price):
    return cups * price

my_bill = calculate_bill(3, 20)
print(f"tabel no 10 bill: {my_bill}")

# can call directly into print
print(f"tabel no 3 bill: {calculate_bill(5, 15)}")

def add_vat(price, vat_tax):
    return price * (100 + vat_tax)/100

orders_price = [100,120, 500, 210, 80, 800]

for price in orders_price:
    total_amount = add_vat(price, 10)
    print(f"the orders amount is {price} and total amount with tax is {total_amount}")

'''
Variable Scope (Local vs. Global)
Local Scope: Variables created inside a function exist only within that function.

Global Scope: Variables defined outside functions are accessible everywhere, 
though modifying them inside a function requires the global keyword.
'''

def serve_chai():
    chai_name = "masala" # local
    print(f"local scope :{chai_name}")
chai_name = "cinnomon" # outside
print(f"outside function scope : {chai_name}")

serve_chai()

def order_menu():
    chai_order = "Tea" # enclosing
    def near_table_order():
        chai_order = "matcha" # Inner
        print(f"Inner: {chai_order}")
    near_table_order()
    print(f"outer:{chai_order}")
chai_order = "bubble Tea"
print(f"Global:{chai_order}")
order_menu()

'''
The nonlocal keyword in Python is used inside nested functions to modify a variable that belongs to an outer (enclosing) function,
 without making it global.

The Problem nonlocal Solves
In Python, an inner function can read variables from its enclosing outer function. 
However, the moment you attempt to reassign that variable, Python treats it as a brand-new local variable inside the inner function:
'''
def serve_order():
    order = "Pongal"
    def kitchen():
        nonlocal order
        order = "Dosa"
    kitchen()
    print(f"chef says now only available is {order}")

serve_order()

'''
The global keyword in Python allows a function to modify a variable defined at the top (module) level of a script,
 rather than creating a local variable of the same name.

The Problem global Solves
In Python, you can freely read a global variable inside a function:
'''

global_order = "Plain Dosa"

def at_counter():
    global global_order
    print(f"global order is {global_order}")

at_counter()

def front_desk():
    def chef_making():
        global global_order
        global_order = "Egg Dosa"
        print(f"please wait chef is making {global_order}")
    chef_making()

front_desk()
print(f"Global order gets manupulates {global_order} so use global very carefully")

def lisings_manuplate(li):
    li[1] = 43
    print(f"manplate lists :{li}") # manplate lists :[1, 43, 6, 7]

lists = [1,4,6,7]
lisings_manuplate(lists)

def make_args(ord, timess):
    print(f"{ord}, {timess}")

make_args("darjee", 30)
make_args(timess=60, ord="kneyyy") # If provide key arguments then where ever position it will map correctly

def make_key_args(*incredients, **extras):
    print(f"{incredients} and {extras}")

make_key_args("ginger", "tea leaves", sweet="sugar", cubes="3", elachi= "Yes") # for * no need of key it's optional to it but for ** key arguments are mandatory and both incredients and extras returns data in tuples for * and for ** in object format

def take_something(orderm=[]):
    orderm.append("Hi")
    print(f"{orderm}")

take_something() # ['Hi']
take_something() # ['Hi', 'Hi'] this type of mistakes may happen so always use none

def repeat_above(orderm=None):
    if orderm is None:
        orderm = []
        orderm.append("Hi")
    print(f"{orderm}")

repeat_above() # ['Hi']
repeat_above() # ['Hi']

def without_return():
    print("No retun means none")

none_comes = without_return()
print(none_comes) # None

# Early Return

def work_status(tickets):
    if tickets == 0:
        return print("Congrats, All tickets completed")
    return print(f"{tickets} are still pending")

work_status(0) # Congrats, All tickets completed
work_status(2) # 2 are still pending

# multiple values 

def multiple_values(sold, returns):
    return sold, returns

sold, remainig = multiple_values(100, 30)
print(f"Sold : {sold}") # Sold : 100
print(f"Remaining : {remainig}") # Remaining : 30

#recursive function (the function calls it self)

def recursive_func(n):
    print(n)
    if n == 1:
       return print("only one is left in this recursive function")
    return recursive_func(n-1)

recursive_func(4) 
'''
4
3
2
1
only one is left in this recursive function
'''

chai_types = ['light', 'kadak', 'strong', 'kadak', 'sweet', 'kadak']

# lambda means ananymous function or name less function

only_kadak = list(filter(lambda chai: chai == 'kadak', chai_types))

print(f"{only_kadak}") # ['kadak', 'kadak', 'kadak']

# built in functions example 

def built_in_funct(somevalue = "some value"):
    """
    this is the link of bulit in functions 
    https://docs.python.org/3/builtins/functions.html
    """
    name_to_find = "something"
    return somevalue, name_to_find

print(built_in_funct.__doc__) # this is the link of bulit in functions https://docs.python.org/3/builtins/functions.html
print(built_in_funct.__name__)  # built_in_funct