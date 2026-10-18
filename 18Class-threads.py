'''
what is Concurrency and Parallelism?
Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once.
Concurrency: Managing multiple computations at the same time by switching between them (interleaving). 
A single-core CPU can run tasks concurrently through rapid context switching.

Parallelism: Executing multiple computations simultaneously at the exact same physical instant on separate hardware CPU cores.

What is Thread?
A thread is the smallest unit of execution within an operating system process.
Threads belonging to the same process share the same memory space, global variables, and open files.

In Python, OS-level threads are managed via the standard threading module.

'''
import threading
import time
from  multiprocessing import Process

def take_order():
    for i in range(1, 4):
        print(f"Taking order for {i}")
        time.sleep(1)

def brew_tea():
    for i in range(1,4):
        print(f"Brewing Tea for {i}")
        time.sleep(2)

# threading 
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_tea)

order_thread.start()
brew_thread.start()

# join 
order_thread.join()
brew_thread.join()

def brew_coffee(name):
    print(f'start time {name}')
    time.sleep(2)
    print(f'stop time {name}')

if __name__ == "__main__":
    cofee_makers = [
        Process(target=brew_coffee, args=(f"Coffee maker {i+1}" ,)) for i in range(3)
    ]

    # start all process 
    for p in cofee_makers:
        p.start()
    # end of all process
    for n in cofee_makers:
        n.join()