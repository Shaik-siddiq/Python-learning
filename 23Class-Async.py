import asyncio
import aiohttp
'''
Python's asyncio framework enables writing concurrent code using the async/await syntax. 
It is primarily used for I/O-bound operations (such as network requests, database queries, and file operations) 
where execution spends significant time waiting for external operations to complete
'''
"""
Synchronous vs. Asynchronous:

Synchronous execution blocks the execution thread until an operation completes.

Asynchronous execution yields control back to the event loop while waiting for an operation, allowing other tasks to run concurrently on a single thread.

Event Loop: The runtime coordinator in asyncio. It manages, schedules, and executes asynchronous tasks and handles I/O events.

Coroutines: Functions declared with async def that can be paused and resumed using await.

Awaitable Objects: An object that can be used in an await expression. The three primary types are Coroutines, Tasks, and Futures. 
"""

"""
async def (Defining Coroutines)
The async def syntax defines a coroutine function. 
Calling a coroutine function does not immediately run its body, instead it returns a coroutine object.

await (Yielding Control)
The await keyword suspends execution of the enclosing coroutine until the awaitable object completes and returns its result.

await can only be used inside an async def function.

When a coroutine hits an await, control returns to the Event Loop, allowing other scheduled tasks to progress.

asyncio.run()
Introduced in Python 3.7+, asyncio.run(coro) serves as the standard entry point for an asynchronous program:

Creates a new event loop.

Runs the passed coroutine until completion.

Closes the loop and cleans up asynchronous generators and tasks.
"""

async def get_a_runner():
    return "Siddiq Running"

async def brew_tea():
    print("Breawing tea")
    await asyncio.sleep(2)
    print(f"Berwed Tea")
    # running = await "Siddiq runing" # TypeError: 'str' object can't be awaited
    runner = await get_a_runner()
    print(f"{runner}")

asyncio.run(brew_tea())

"""
Differences 

{
  "definition": {
    "javascript": "A built-in runtime concurrency coordinator that continuously checks the call stack and transfers pending callbacks from the microtask and macrotask queues to execute non-blocking asynchronous code on a single thread.",
    "python": "An explicit user-level scheduling engine (provided by asyncio) that manages, pauses, and resumes generator-based coroutines and polls OS-level I/O selectors (epoll/kqueue) within an iteration loop on a single thread."
  },
  "runtime_integration": {
    "javascript": "Native to the runtime engine (V8, JavaScriptCore, SpiderMonkey, libuv); permanently active and inescapable.",
    "python": "Standard library module (asyncio); opt-in, must be explicitly instantiated and started."
  },
  "default_execution_mode": {
    "javascript": "Top-level code runs automatically inside an active event loop.",
    "python": "Execution is synchronous by default until invoked via asyncio.run()."
  },
  "queue_architecture": {
    "javascript": "Hierarchical multi-queue system: Call Stack -> Microtask Queue (Promises, queueMicrotask) -> Macrotask Queue (setTimeout, I/O events, setImmediate in Node).",
    "python": "Single flat architecture: an internal deque for ready tasks (_ready) and a min-heap priority queue for scheduled timer delays (_scheduled)."
  },
  "task_priority_rule": {
    "javascript": "Microtasks have absolute priority; the Microtask Queue is completely drained before a single macrotask executes.",
    "python": "No strict microtask vs macrotask tiering; tasks in the ready queue execute sequentially as the loop turns (FIFO/step iterations)."
  },
  "underlying_primitive": {
    "javascript": "Promises, callback queues, and engine-level event emitters.",
    "python": "Generators, coroutine objects, and the iterator stepping protocol (__await__, yield from, .send(None))."
  },
  "loop_pluggability": {
    "javascript": "Rigid; baked directly into the host platform (browser Web APIs or Node.js libuv bindings).",
    "python": "Pluggable and replaceable via the AbstractEventLoop interface (e.g., using uvloop for C-based libuv speeds)."
  },
  "threading_and_event_loops": {
    "javascript": "Single primary event loop per JavaScript runtime context/worker thread.",
    "python": "One event loop per OS thread by default; multiple distinct threads can each run their own independent asyncio loop."
  },
  "implicit_type_coercion": {
    "javascript": "Permissive; await automatically wraps non-Promise values using Promise.resolve(x).",
    "python": "Strict; await demands objects explicitly implementing the __await__() protocol, raising TypeError otherwise."
  }
}

"""

# event loop example


async def brew_chai(name, time):
    return print(f"serving {name} in {time} min")


async def chai_serve():
    await asyncio.gather(
        brew_chai("Masala chai", 2),
        brew_chai("ginger Chai", 1),
        brew_chai("Lemon Tea", 3)
    )

asyncio.run(chai_serve())

# http requests

async def fetch_url(url, session):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
        return response.status

async def main_url():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        result = await asyncio.gather(*task) # * works like spread operator of js like in an array t = [1,2,3] ,  [...t] both will give same output in JS
        print("All Done:", result) # All Done: [200, 200, 200]

asyncio.run(main_url())


