'''
Classes vs. Instances
Class (Origin): A blueprint and an object in its own right. It holds shared state, methods, and configurations.

Instance (originates = Origin()): A distinct entity instantiated from the class.
 It retains independent state while looking up shared definitions from the class.
'''
class Origin:
    country = "India"
    language = "No national language"

print(Origin.country)

Origin.capital = "Delhi"
originates = Origin()
Origin.is_hot = True
print(f"from class Origin: {Origin}") #from class Origin: <class '__main__.Origin'>
print(f" from class derived object originates : {originates}") # from class derived object originates : <__main__.Origin object at 0x10f4a0590>
print(f" {originates.is_hot}") # True
'''
Attribute Shadowing
Shadowing occurs when an instance is given an attribute with the exact same name as an existing class attribute.

When you write instance.attr = value, Python never alters the class attribute.
Instead, it creates a new entry inside that instance's personal namespace, "shadowing" (masking) the class version for that instance.
'''
originates.is_hot = False
print(f"{originates.is_hot}")  # False
originates.population = "1.21 Billion"
originates.language = "Hindi/Urdu"
# print(Origin.population) We can't assing from instance to class , it will throw error as AttributeError: type object 'Origin' has no attribute 'population'
print(originates.population) # 1.21 Billion
print(f"language from instance originates : {originates.language}") # language from instance originates : Hindi/Urdu
print(f"language from class itself: {Origin.language}") #language from class itself: No national language

del originates.language
print(f"After deleting language from oginate then it fall backs to main class Origin: {originates.language}") # After deleting language from oginate then it fall backs to main class Origin: No national language


'''
In Python, self represents the specific instance of the class that is currently calling the method.

Whenever you call an instance method like originates.describe(), 
Python automatically passes the instance originates as the very first argument behind the scenes:
'''

class states:
    state = "Andhar"
    capital = "Amaravathi"
    def describe(self):
        return f"the state is {self.state} and capital is {self.capital}"

state_1 = states()
print(state_1.describe()) # the state is Andhar and capital is Amaravathi
# If we want print directly class, if we don't pass object inside params of class function then it will throw error as TypeError: states.describe() missing 1 required positional argument: 'self'
print(f" Directly States class is printing : {states.describe(state_1)}") # Directly States class is printing : the state is Andhar and capital is Amaravathi

state_2 = states()
state_2.state = "Kerela"
state_2.capital = "Kochi"
print(state_2.describe()) # the state is Kerela and capital is Kochi
print(f" from class states: {states.describe(state_2)}") #  from class states: the state is Kerela and capital is Kochi

'''
Instance Attribute
__init__ is Python's initializer method (often called the constructor).
 When you create a new object from a class, Python automatically calls __init__ behind the scenes to attach data—known as instance attributes—directly to that newly created object.
Inside __init__ (or assigned via self.attr)	
Specific to that single instance	
Modifying instance.attr affects only that specific instance.
'''
class instance_attribute:
    def __init__(self, name, size):
        self.anyword = name
        self.anysize = size

instance_1 = instance_attribute("small scale", "15cm")
print(instance_1.anyword) # small scale
print(instance_1.anysize) # 15cm

instance_2 = instance_attribute("big scale", "30cm")
print(instance_2.anyword , instance_2.anysize) # big scale 30cm

'''
Inheritance and Composition are the two primary ways to share and reuse code between classes in object-oriented programming.

The core distinction boils down to the relationship between your classes:

Inheritance represents an "IS-A" relationship (a Dog is an Animal).

Composition represents a "HAS-A" relationship (a Car has an Engine).

 Inheritance ("IS-A")
In inheritance, a child class derives all methods and attributes from a parent class. 
The child can use them directly, extend them using super(), or override them completely.

When to use Inheritance:
A child class is genuinely a specialized subtype of the parent class (Liskov Substitution Principle: anywhere a Vehicle works, an ElectricCar should work too).

You want shared default behavior across many closely related subclasses.
'''
class vehical:
    def __init__(self, brand):
        self.carBrand = brand
    def start(self):
        return f"the car brand is {self.carBrand}"

class electricVehical(vehical):
    def __init__(self, brand, kwh):
        super().__init__(brand)
        self.Batterykwh = kwh 
    def startEv(self):
        return f"The Car is {self.carBrand} and battery is {self.Batterykwh} "

class petrolVechical(vehical):
    def __init__(self, brand, horsepower):
        super().__init__(brand)
        self.hp = horsepower
    def startHp(self):
        return f"The Car is {self.carBrand} and power is {self.hp}"

ev = electricVehical("Tesla", "12KWH")
petrolCar = petrolVechical("TaTa", "1199cc")

print(ev.start()) # the car brand is Tesla
print(ev.startEv()) # The Car is Tesla and battery is 12KWH 
print(petrolCar.start()) # the car brand is TaTa
print(petrolCar.startHp()) # The Car is TaTa and power is 1199cc

'''
Composition ("HAS-A")
In composition, a class does not inherit from another class; instead, 
it contains one or more instances of other classes as attributes and delegates tasks to them.
When to use Composition:
Components need to be swapped or configured independently 
(e.g., swapping an ElectricMotor for a V8Engine without rewriting the Car class).
Objects are made up of loosely coupled parts rather than natural biological-style hierarchies.
'''

# this is with init 
class Engine:
    def __init__(self, horse_power=int):
        self.hp = horse_power
    def engineStart(self):
        return f"vroom vroom V8 engine with {self.hp} HP"

# this is without init
class soundTrack:
    def playsong(self, track=str):
        return f"playing song {track}"

class car_model:
    def __init__(self, brand, horsePower:int):
        self.brand = brand
        self.engine = Engine(horsePower)
        self.musicOn = soundTrack()
    def trip(self, track=str):
        engine_start= self.engine.engineStart()
        music = self.musicOn.playsong(track)
        return f"The car is {self.brand} \n start, {engine_start} \n {music}"

tripDetails = car_model("Ford", 1900)
print(tripDetails.trip("Ye kya baat hai ajj"))   

'''
output 
The car is Ford 
 start, vroom vroom V8 engine with 1900 HP 
 playing song Ye kya baat hai ajj
'''

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

    bot = RoboToy(model_name="CyberHound X1", robot_type="Robo-Dog", price=149.99, battery_level=85)

print(bot)
# Output: RoboToy(model='CyberHound X1', type='Robo-Dog', price=$149.99, battery=85%)

# Reading via getters:
print(bot.price)            # Output: 149.99
print(bot.battery_level)    # Output: 85
print(bot.is_operational)   # Output: True