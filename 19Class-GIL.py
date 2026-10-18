'''
1. Python and the GIL
What the GIL Is?
The GIL is a mutual exclusion lock (mutex) used by CPython—the standard Python implementation—to ensure that only one OS thread executes Python bytecode at a time.  
Why it exists: CPython uses reference counting for memory management. Without the GIL, multiple threads mutating object reference counts simultaneously would corrupt internal interpreter memory.
The consequence: Python multithreading does not provide parallel execution for CPU-bound tasks. 
Multiple threads will contend for the lock on multi-core systems, often running slower than a single thread. 
(Note: In Python 3.13+, experimental free-threaded builds allow disabling the GIL).   
Does the GIL Prevent Race Conditions in Python?
No. This is a common misconception.The GIL ensures interpreter safety (reference counts and internal C structs won't corrupt).  
The GIL does not ensure application-level thread safety.
Python automatically preempts threads by releasing and re-acquiring the GIL after executing a certain number of bytecode instructions (or every 5ms by default). 
If a Python operation is composed of multiple bytecode steps (like read-modify-write), a context switch can occur mid-operation. 
'''

import threading
import time
from multiprocessing import Process

def brew_honey():
    print(f"{threading.current_thread().name} Start the threading")
    count = 0
    for _ in range(100_000_000):
        count +=1
    print(f"{threading.current_thread().name} finished threading")


def crunch():
    print(f"Start the count process")
    count = 0
    for _ in range(100_000_000):
        count +=1
    print(f"End of process count")

# EVERYTHING that triggers actions must live under this guard:
if __name__ == '__main__':
    # --- 1. Threading (Bound by GIL) ---
    t1 = threading.Thread(target=brew_honey, name="jasmine")
    t2 = threading.Thread(target=brew_honey, name="Rose")
    start_t = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    end_t = time.time()
    print(f"Total time taken {end_t-start_t:.2f} seconds") # Total time taken 4.80 seconds\
    # --- 2. Multiprocessing (Independent GIL per process) ---
    p1 = Process(target=crunch)
    p2 = Process(target=crunch)
    start1 = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    end2 = time.time()
    print(f"Total time taaken by multiprocessing is {end2-start1:.2f} seconds")

def boil_milk():
    print(f"Boliing the milk")
    time.sleep(2)
    print(f"BOILED MILK...")

def toast_bun():
    print(f"tosting the bun..")
    time.sleep(3)
    print(f"Bun Toasted")

start = time.time()
m1 = threading.Thread(target=boil_milk)
m2 = threading.Thread(target=toast_bun)

m1.start()
m2.start()
m1.join()
m2.join()

end = time.time()
print(f"Breakfast ready at {end-start:.2f}...")

def prepare_something(type_, wait):
    print(f"{type_} brewing ...")
    time.sleep(wait)
    print(f"{type_} finished brewing ...")

if __name__ == "__main__":
    n1 = threading.Thread(target=prepare_something, args=("s1", 2))
    n2 = threading.Thread(target=prepare_something, args=("s2", 4))
    start = time.time()

    n1.start()
    n2.start()
    n1.join()
    n2.join()
    end = time.time()
    print(f"This taken time is {end-start:2f}")
