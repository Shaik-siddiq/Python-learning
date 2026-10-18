import threading
import time
from multiprocessing import Process, Queue, Value
from ctypes import c_bool

'''
Process is always faster than threading
'''

def cup_heavy():
    print(f"crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += i
    print(f"Done ✅")

# start = time.time()
# threads = [threading.Thread(target=cup_heavy) for _ in range(2)] 
# [i.start() for i in threads]
# [i.join() for i in threads]

# print(f"Time taken: {time.time()-start:2f} seconds")
"""
crunching some numbers...
crunching some numbers...
Done ✅
Done ✅
Time taken: 7.160025 seconds
"""
if __name__ == '__main__':
    processess = [Process(target=cup_heavy) for _ in range(2)]
    start = time.time()
    [t.start() for t in processess]
    [t.join() for t in processess]
    print(f"Time taken proccess: {time.time()-start:2f} seconds") # Time taken proccess: 3.703007 seconds

"""
Multiprocessing with Queue and Value
In Python's multiprocessing module, processes do not share memory space like threads do. 
To communicate or share state between them, 
you must use inter-process communication (IPC) tools such as Queue (for message passing) and Value (for shared scalar variables).

Why is Multiprocessing Faster than Threading in Python?
Whether multiprocessing is faster depends on the workload. 
For CPU-bound tasks, multiprocessing dramatically outperforms standard threading due to CPython's GIL (Global Interpreter Lock).
[
  {
    "dimension": "GIL Impact",
    "multiprocessing": "Bypassed completely. Each process gets its own Python interpreter and memory space, enabling true parallelism on multi-core CPUs.",
    "threading": "Constrained. Only one thread can execute Python bytecode at a time, even on a multi-core CPU."
  },
  {
    "dimension": "Best Used For",
    "multiprocessing": "CPU-heavy computation (math, video/image processing, parsing large datasets, encryption).",
    "threading": "I/O-bound tasks (network requests, database calls, reading/writing disk)."
  },
  {
    "dimension": "Memory & Startup Overhead",
    "multiprocessing": "Higher (spawns separate OS processes with duplicate interpreter instances and memory allocations).",
    "threading": "Low (lightweight OS threads sharing the same heap and memory)."
  },
  {
    "dimension": "Data Sharing",
    "multiprocessing": "Requires IPC (Queue, Pipe, shared_memory, Value). Objects must be serialized via pickle.",
    "threading": "Direct in-memory access to Python objects, but requires manual locks (threading.Lock)."
  }
]
"""
def prepare_whatever(queue):
    queue.put("Something is ready....")

queue = Queue()
if __name__ == "__main__":
    p = Process(target=prepare_whatever, args=(queue, ))
    p.start()
    p.join()
    print(queue.get()) # Something is ready....


# value 

def worker_task(is_running: Value):
    print("Worker: started processing stream...")
    count = 0
    # Read the shared boolean flag
    while is_running.value:
        count += 1
        time.sleep(0.3)
        print(f"Worker: processed batch {count}")
    
    print("Worker: received shutdown signal, cleaning up and exiting.")

if __name__ == "__main__":
    # Create a shared boolean initialized to True
    keep_running = Value(c_bool, True)

    process = Process(target=worker_task, args=(keep_running,))
    process.start()

    # Let the worker run for 1 second in the background
    time.sleep(1.0)

    # Main process signals the worker to halt
    print("Main: telling worker to stop!")
    with keep_running.get_lock():
        keep_running.value = False

    process.join()
    print("Main: worker safely shut down.")