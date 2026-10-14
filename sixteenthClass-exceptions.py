'''
error handling allows your program to intercept unexpected runtime errors and handle them gracefully instead of crashing abruptly.
Error / Exception: An event detected during execution that interrupts normal program flow 
(e.g., ZeroDivisionError, ValueError, FileNotFoundError).

try: Wraps the block of code that might trigger an exception.

except: Catches and handles specific exceptions if they occur in the try block.

else: Runs only if the try block completes successfully without any exceptions.

finally: Runs always, regardless of whether an exception occurred, was caught, 
or was uncaught (ideal for cleanup tasks like closing files or database connections).
'''

'''
Best Practices
Avoid bare except:: Writing except: without an exception type catches SystemExit, KeyboardInterrupt (Ctrl+C), and hides bugs. 
Always specify the exception type, or at least catch except Exception:.

Keep try blocks narrow: Only put lines of code inside try that you reasonably expect might fail.

Use else to prevent false catches: If code shouldn't be protected by the except handler, place it in else rather than inside try.
'''

try:
    num = int(input('Enter a number : '))
    result = 100/num
except ZeroDivisionError:
    # 1. Handles division by zero
    print("Error : you can not divide by zero")
except ValueError:
    # 2. Handles invalid input (e.g., typing 'abc')
    print("Error: only numbers are allowed")

else:
    # 3. Executes ONLY if try raised no exceptions
    print(f"Here is the result: {result}")
finally:
    # 4. Executes NO MATTER WHAT
    print("Cleanup complete: Execution finished.")

try:
    with open("data.txt", "r") as f:
        content = f.read()
        value = int(content.strip())
        output = 50/value
except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print("Error: this file has no integer")
else:
    print(f"The numbers in the file is: {output}")

# your own excepition

def brew_chai(flavour):
    flavours = ["masala", "Ginger", "Elachi"]
    if flavour not in flavours:
        raise ValueError("Unsupported Chai flavour.....")
    print(f"{flavour} is brewing")

brew_chai("Ginger") 

# custom Exception

class missingIncredients(Exception):
    pass

def make_coffee(item):
    if item not in ["water", "cofee powder", "honey"]:
        raise missingIncredients("missing honey")
    return print(f"brewing black coffee")
make_coffee("honey")

# mini excercise 

class missingCarName(Exception): pass

def BuyCar(carname, noOfcars):
    deck = {"Volswagan":48, "BMW":132, "TATA":8, "Maruthi":3, "Ford":40}
    try:
        if carname not in deck:
            raise missingCarName(f"The {carname} is not present , please select from {deck.keys}")
        if not isinstance(noOfcars, int):
            raise TypeError(f"{noOfcars} should be integer")
        total = deck[carname] * noOfcars
        print(f"The care name is {carname} and no of cars you selected {noOfcars} and the Bill is {total}L ")
    except Exception as e:
        print(f"Error is {e}")
    finally:
        print("Please visit again")

BuyCar("TATA", 3)
BuyCar("SALSA", 2) # Error is The SALSA is not present , please select from <built-in method keys of dict object at 0x10d2fe640>
BuyCar("Maruthi", "Four") # Error is Four should be integer

        