import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypting(data):
    return f"🔒 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as Pool:
        result = await loop.run_in_executor(Pool, encrypting, "Lock_01_ABC")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
        