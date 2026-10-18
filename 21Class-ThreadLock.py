'''
In Python, threading.Lock() provides a mutual exclusion primitive (commonly known as a mutex). 
Its primary job is to prevent race conditions by ensuring that only one thread can execute a critical section of code or access a shared resource at any given moment.

Why It Is Needed: The Problem
Python's standard memory model allows threads to run concurrently and share variables. 
If multiple threads read, modify, and write to a shared variable at the same time, operations can interleave unexpectedly.

Even simple lines like counter += 1 are not atomic under the hood—they consist of three distinct bytecode steps:

Load value of counter

Add 1 to the loaded value

Store the result back into counter

If a thread switch occurs between loading and storing, one thread's update overwrites another's, resulting in lost updates.

Core Mechanics & State
A lock exists in one of two states: unlocked (default) or locked.

acquire(blocking=True, timeout=-1):

If the lock is unlocked, calling acquire() sets it to locked and returns True immediately.

If the lock is already locked, the calling thread blocks (pauses execution) until another thread releases it.

If blocking=False, it does not wait; it returns True if acquired, or False immediately if locked.

release():

Changes the state back to unlocked.

Wakes up one of the waiting threads to acquire the lock.

Calling release() on an unlocked lock raises a RuntimeError.
'''

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter +=1

t1 = [threading.Thread(target=increment) for _ in range(10)]

[t.start() for t in t1]
[t.join() for t in t1]

print(f"Final counter count is {counter}") # Final counter count is 10000

'''
Key Takeaways & Best Practices
Scope tightly: Keep the block inside with lock: as short as possible to avoid serializing your code and negating concurrency benefits.

Avoid deadlocks: If multiple locks are required, always acquire them in the exact same order across all threads.

GIL interaction: While Python's Global Interpreter Lock (GIL) ensures memory integrity at the CPython interpreter level, 
it does not protect application-level shared state from race conditions. threading.Lock() is still required.
'''