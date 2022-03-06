import asyncio
import time

"""

    Shows how to delay a task, creating a 'schedule'
    
    Can use time here to break up our many tasks, 
        by creating our tasks with an incremented delay.
    
"""

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

    
async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
