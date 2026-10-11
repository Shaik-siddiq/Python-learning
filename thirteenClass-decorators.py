from functools import wraps

'''
A decorator in Python is a design pattern and language feature that allows you to dynamically modify or extend the behavior of a function or class without altering its actual source code.

Under the hood, functions in Python are first-class citizens—they can be passed as arguments, assigned to variables, 
and returned from other functions. A decorator takes a function as input, 
wraps it with extra behavior, and returns the modified function:

Why Use Decorators?
Decorators let you adhere to the Single Responsibility Principle and DRY (Don't Repeat Yourself).
 Instead of littering cross-cutting concerns (like timing, authorization, and logging) across dozens of functions,
 you write the concern once and attach it via @.
 1. Execution Timing & Benchmarking
 2. Caching & Memoization
 3. Authentication & Authorization (Web Frameworks)
 4. Input Validation & Type Checking
 5. Retry Mechanism with Exponential Backoff
 
'''

def my_decorators(func):
    print("My decorator")
    def wrapper():
        func()
        print(' Inside wrapper')
    return wrapper

@my_decorators
def greet():
    print("Hello from decorators")

greet()
'''
output 
My decorator
Hello from decorators
 Inside wrapper
'''
def decorators_example2(func):
    @wraps(func)
    def wrapLogactivity(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapLogactivity

@decorators_example2
def brewing_coffee(type, milk="No"):
    return print(f"Brewing {type} and milk add: {milk}")

brewing_coffee("Black Coffee")

'''
output 
calling brewing_coffee
Brewing Black Coffee and milk add: No
Finished brewing_coffee
'''

def require_admin(func):
    @wraps(func)
    def wrapper(user):
        if user == "admin":
            print("Authorization Done")
            func(user)
        else:
            print("Access Denied : only Admin access")
        return user
    return wrapper

@require_admin
def access_inventory(user):
    print(f"{user} welcome to inventory")

access_inventory("user") # Access Denied : only Admin access
access_inventory("admin") 
'''
Authorization Done
admin welcome to inventory
'''

