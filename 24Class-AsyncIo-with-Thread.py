import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

def check_store(item):
    print(f"{item} Checking stocks")
    time.sleep(2)
    return f"{item} is : 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
       result = await loop.run_in_executor(pool, check_store, "Ginger")
       print(result)

asyncio.run(main())
