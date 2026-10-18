'''
Method Resolution Order (MRO) is the exact path Python follows when searching for an attribute or method across a class hierarchy.

When you call instance.method(), Python does not search randomly; 
it scans a strictly ordered, linear list of classes. The first class in that list containing the method wins.
1. Viewing the MRO
You can inspect any class's resolution order directly using either the mro() method or the __mro__ attribute:
2. The Classic "Diamond Problem"
MRO becomes essential during multiple inheritance, especially in a diamond-shaped hierarchy:
You can inspect any class's resolution order directly using either the mro() method or the __mro__ attribute:
       A
      / \
     B   C
      \ /
    D or E
'''

class A:
    lable = "Class A"

class B(A):
    lable = "Class A changed to Class B"

class C(A):
    lable = "Class A changed to Class C"

class D(B, C):
    pass
class E(C, B):
    pass

cup = D()
cup_1 = E()
print(cup.lable) # Class A changed to Class B
print(cup_1.lable) # Class A changed to Class C

print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(E.__mro__) # (<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

'''
A static method in Python is a method bound to a class that does not receive an implicit first argument—it accesses neither the instance (self) nor the class (cls).

It behaves like an ordinary, plain function, but lives inside the class's namespace for logical grouping and organization.
How to Define and Call It
Use the @staticmethod decorator above the function definition:
'''

class Chai_incredients:
    @staticmethod
    def chai(text):
       return [item.strip() for item in text.split(",")]

incredients = "Milk, tea_powder, sugar, water"
items = Chai_incredients.chai(incredients)
print(items) # ['Milk', 'tea_powder', 'sugar', 'water']

'''
A class method in Python is a method that receives the class itself as its implicit first argument (cls),
 rather than an instance of the class (self).

It is marked using the @classmethod decorator and operates on class-level data rather than individual object state.
'''
class Bed:
    def __init__(self, bed_type, bed_size):
        self.bed_size = bed_size
        self.bed_type = bed_type
    @classmethod
    def from_dict(cls, queen_bed):
        return cls(
        queen_bed["bed_type"],
        queen_bed["bed_size"]
        )
    @classmethod
    def from_str(cls, instring):
        bedtype, bedsize = instring.split("-")
        return cls(bedtype, bedsize)

order1 = Bed.from_dict({"bed_type":"Queen Bed", "bed_size":"5 X 7"})
order2 = Bed.from_str("King-7X8")
print(order1.__dict__) # {'bed_size': '5 X 7', 'bed_type': 'Queen Bed'}
print(order2.__dict__) # {'bed_size': '7X8', 'bed_type': 'King'}

'''
property decorator
In Python, the @property decorator allows you to turn a method into a managed attribute. 
This gives you getter, setter, and deleter functionality while keeping a clean syntax—so 
you access obj.price like a standard variable rather than calling obj.get_price() or obj.set_price(100).
'''

class RoboToy:
    def __init__(self, model_name: str, robot_type: str, price: float, battery_level: int = 100):
        self.model_name = model_name
        self.robot_type = robot_type  # e.g., "Transformer", "Humanoid", "Dog"
        
        # Both setters run here during object creation!
        self.price = price
        self.battery_level = battery_level

    # ==========================
    # 1. PRICE (Getter, Setter, Deleter)
    # ==========================
    @property
    def price(self) -> float:
        """Read access for price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Write access with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(value)

    @price.deleter
    def price(self):
        """Reset price to default promo or 0.0."""
        print(f"Clearing price tag for {self.model_name}...")
        self._price = 0.0

    # ==========================
    # 2. BATTERY LEVEL (Getter & Setter with bounds check)
    # ==========================
    @property
    def battery_level(self) -> int:
        """Read access for battery percentage."""
        return self._battery_level

    @battery_level.setter
    def battery_level(self, percentage: int):
        """Ensure battery stays strictly between 0 and 100%."""
        if not isinstance(percentage, (int, float)):
            raise TypeError("Battery percentage must be numeric.")
        if not (0 <= percentage <= 100):
            raise ValueError("Battery level must stay within 0% to 100%.")
        self._battery_level = int(percentage)

    # ==========================
    # 3. COMPUTED READ-ONLY ATTRIBUTE (Getter only)
    # ==========================
    @property
    def is_operational(self) -> bool:
        """Determines if the robot can perform actions."""
        return self._battery_level > 5

    def __repr__(self):
        return (f"RoboToy(model='{self.model_name}', type='{self.robot_type}', "
                f"price=${self.price}, battery={self.battery_level}%)")


# ========================================================
# Out of the class body (no indentation):
# ========================================================
bot = RoboToy(model_name="CyberHound X1", robot_type="Robo-Dog", price=149.99, battery_level=85)

print(bot)
print(bot.price)            # Output: 149.99
print(bot.battery_level)    # Output: 85
print(bot.is_operational)   # Output: True

'''
In Python, decorators are tools for modifying functions or methods dynamically, 
while getters and setters are object-oriented mechanisms used to access and mutate an object's internal state safely.
'''
'''
What is a Decorator?
A decorator is a callable (usually a function) that takes another function as an argument, extends or alters its behavior without modifying its source code, and returns the modified function.

They rely on the fact that functions in Python are first-class citizens—meaning they can be passed as arguments, assigned to variables, and returned from other functions.
'''
def mainfunc(func):
    def announce(*args, **kargs):
        print("Execution Started")
        result = func(*args, **kargs) # if we don't keep * and ** here then we will get error as result = func(args, kargs) TypeError: greet() takes 1 positional argument but 2 were given
        print(f"Excecution compled:")
        return result
    return announce

@mainfunc
def greet(name):
    print(f"hello {name}")

greet("siddiq")
'''
output
Execution Started
hello siddiq
Excecution compled:
'''

'''
 The @property Decorator
with the @property decorator. It turns method calls into what look like standard attribute lookups, 
letting you enforce validation, logging, or dynamic calculation behind the scenes without breaking your public API.

Getter (@property): Defines the method that runs when accessing obj.attribute.

Setter (@<name>.setter): Defines the method that runs when assigning a value with obj.attribute = value.

Deleter (@<name>.deleter): Defines what happens when calling del obj.attribute.
'''
class Temperature:
    def __init__(self, celcius):
        # Calls the setter directly during initialization
        self.celcius = celcius

    # 1. Getter
    @property
    def celcius(self):
        return self._celcius

    # 2. Setter (adds validation)
    @celcius.setter
    def celcius(self, value):
        if value < 24:
             raise ValueError("The temprature has gone below room temperate, please maintain room temperate")
        self._celcius = value

    # 3. Read-only computed property (getter only)
    @property
    def fahrhenheit(self):
        return (self._celcius * 9/5) + 32

temp = Temperature(26)
# Accessing values like normal attributes (triggers getters)
print(temp.celcius)      # 26
print(temp.fahrhenheit)   #  78.8

# Modifying a value (triggers setter validation)
temp.celcius = 32
print(temp.celcius) # 32
print(temp.fahrhenheit) # 89.6

# Validation failure
try:
    temp.celcius = 23
except ValueError as e:
    print(e)  # The temprature has gone below room temperate, please maintain room temperate

# Read-only property check
try:
    temp.fahrhenheit = 100
except AttributeError as e:
    print(e) # property 'fahrhenheit' of 'Temperature' object has no setter

