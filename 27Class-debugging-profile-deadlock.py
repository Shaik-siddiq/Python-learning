"""
Debugging in Python
Modern Python debugging ranges from built-in breakpoint helpers to non-intrusive post-mortem inspection.

Built-in Breakpoints (breakpoint())
Introduced in Python 3.7, breakpoint() drops directly into the debugger configured via PYTHONBREAKPOINT (defaults to pdb):
"""

def calculate_metrics(values):
    total = sum(values)
    breakpoint()  # Drops into interactive pdb session
    return total / len(values)

calculate_metrics()

"""
Essential pdb Commands:

n (next): Execute current line and advance to the next line in the current function.

s (step): Step into the function call at the current line.

c (continue): Resume execution until the next breakpoint.

p <expr> / pp <expr>: Print / pretty-print an expression.

w (where): Show the current call stack trace.

u / d (up/down): Move one frame up or down the call stack.
"""

"""
Post-Mortem Debugging
When an unhandled exception crashes a script, use pdb.pm() to inspect the exact state at failure without rerunning:
python -m pdb -c continue script.py
"""

# exceptions for debugging
#  import sys, pdb

# try:
#     risky_operation()
# except Exception:
#     pdb.post_mortem(sys.exc_info()[2])

"""
Deadlocks in Python
A deadlock occurs when two or more execution threads (or processes) are blocked indefinitely,
 each waiting for a lock or resource held by another.
"""

import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def worker_1():
    with lock_a:
        time.sleep(0.01)
        with lock_b:  # Blocked waiting for lock_b held by worker_2
            print("Worker 1 done")

def worker_2():
    with lock_b:
        time.sleep(0.01)
        with lock_a:  # Blocked waiting for lock_a held by worker_1
            print("Worker 2 done")

t1 = threading.Thread(target=worker_1)
t2 = threading.Thread(target=worker_2)
t1.start()
t2.start()
t1.join()
t2.join()

"""
Profiling Python Applications
Profiling identifies where execution time and memory allocations are concentrated.
[
  {
    "profiler": "cProfile",
    "type": "Deterministic (Event-based)",
    "overhead": "Moderate",
    "best_used_for": "Standard function-level CPU profiling"
  },
  {
    "profiler": "line_profiler",
    "type": "Line-by-line",
    "overhead": "High",
    "best_used_for": "Pinpointing slow loops/lines inside a function"
  },
  {
    "profiler": "py-spy",
    "type": "Sampling",
    "overhead": "Minimal",
    "best_used_for": "Production inspection, active processes"
  },
  {
    "profiler": "tracemalloc",
    "type": "Memory allocation",
    "overhead": "Low–Moderate",
    "best_used_for": "Finding memory leaks & allocation spikes"
  }
]
CPU Profiling with cProfile
python -m cProfile -o profile.prof script.py
# Visualize with snakeviz:
pip install snakeviz
snakeviz profile.prof
"""

"""
Line-Level Profiling (line_profiler)
# script.py
@profile
def slow_loop():
    total = 0
    for i in range(1_000_000):
        total += i**2
    return total
kernprof -l -v script.py
"""

"""
 Memory Profiling with tracemalloc
Built directly into the standard library to identify memory leaks:

import tracemalloc

tracemalloc.start()

# Workload here...
leaky_list = [dict(a=i) for i in range(100_000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:3]:
    print(stat)
    
"""