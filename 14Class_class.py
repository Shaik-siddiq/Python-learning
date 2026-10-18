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