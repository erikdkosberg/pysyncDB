import asyncio
import time

now = time.time()

async def nested():
    now = time.time()
    print(sum([z for z in range(10**7)]))
    

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    later = time.time()
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())

later = time.time()
print(f"{later - now} second(s)")

now = time.time()

print(sum([z for z in range(10**7)]))

later = time.time()
print(f"{later - now} second(s)")
