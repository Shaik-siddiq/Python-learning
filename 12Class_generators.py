'''
A generator in Python is a special type of iterator that generates values on the fly (lazily) instead of computing and storing them all in memory at once.

Standard functions calculate a complete result and return it using return. In contrast, 
a generator pauses its execution and produces items one by one using the yield keyword.

How Generators Work: yield vs return
When Python sees the yield keyword inside a function, calling that function does not run the code immediately. 
Instead, it returns a generator object.

Every time you call next() on the generator (or loop over it with a for loop):

The function runs until it hits yield.

It sends the value back to the caller and freezes its execution state (all local variables and instruction pointers stay preserved).

The next time a value is requested, 
it wakes up right after the yield statement and continues until it hits the next yield or finishes (raising StopIteration).
'''
def order_item ():
    yield  "Ordered Coffee"
    yield  "Ordered Tea"
    yield  "Ordered Jaggery Tea"

# calling generator function by using loop
order_id = 1
for order in order_item():
    print(f"order id {order_id} : {order}")
    order_id +=1

'''
output 
order id 1 : Ordered Coffee
order id 2 : Ordered Tea
order id 3 : Ordered Jaggery Tea
'''

# calling generator function by using next key word
order_1 = order_item()
print(next(order_1))  # Ordered Coffee
print(next(order_1))  # Ordered Tea

'''
Infinite Generator
An infinite generator in Python is a generator function that contains an unbounded loop 
(typically while True:) containing a yield statement.

Because generators evaluate values lazily (only computing the next item when requested), 
an infinite loop never hangs your program or exhausts memory. It simply pauses at each yield until next() is called again.
'''

def infinite_genertor():
    count = 1
    while True:
        yield f"refill {count}"
        count += 1

refill = infinite_genertor()
for _ in range(3):
    print(f"{next(refill)}") # for in range function is used to stop an infinite function run and stop it at certain number

'''
output 
refill 1
refill 2
refill 3
'''
refill2 = infinite_genertor()

for _ in range(5):
    print(f"{next(refill2)}")

'''
the refill and refill2 never colides each have their own output 
refill 1
refill 2
refill 3
refill 4
refill 5
'''

'''
Send Value to Generator
You send values into a generator using its .send(value) method.

In standard usage, yield only outputs values to the caller. 
When used as an expression (received = yield output), 
yield turns the generator into a two-way channel (often called a coroutine): 
it yields data out, pauses, and receives new data sent back in.
'''

def chai_world():
    print(f"What Chai do you Like?")
    order = yield
    while True:
        print(f"Prepaing {order}")
        order = yield # this line is to stop the function, or else it will run to infinite

customer_order = chai_world()
next(customer_order)

customer_order.send("Ginger Tea")
customer_order.send("Lemon Tea")

'''
output
What Chai do you Like?
Prepaing Ginger Tea
Prepaing Lemon Tea
'''
'''
yield from (Delegating to a Subgenerator)
yield from transparently delegates execution from an outer generator to an inner iterable or subgenerator.

It accomplishes two main tasks:

Flattens iterations: Avoids writing manual nested loops (for item in subgen: yield item).

Establishes a transparent bidirectional channel: Forwards values sent via .send(), exceptions raised via .throw(), 
and captures final return values from the subgenerator.
'''

def local_brand():
    yield 'Lava'
    yield 'Jio'

def imported_brand():
    yield 'Iphone'
    yield 'Samsung'

def all_brands():
    yield from local_brand()
    yield from imported_brand()

for all in all_brands():
    print(all)
'''
we can import generation of various function in a single function by using yield from 

Lava
Jio
Iphone
Samsung
'''

def my_gen():
    try:
        while True:
            yield "Working"
    except GeneratorExit:
        print("Generator Colsed")


gen = my_gen()
next(gen)  # Prime generator into try block

run_1 = True


def cannot_run_twice():
    global run_1
    try:
        if run_1:
            print("Run1")
            print(f"{run_1}")
            run_1 = False
            raise Exception("Cannot Run Twice")

        # Second call reaches here because run_1 is False:
        print("Run2")
        gen.close()

    except Exception as e:
        print(f"Error: {e}")
        # Note: Do NOT call gen.close() here, otherwise it dies in Run 1!


cannot_run_twice()
cannot_run_twice()