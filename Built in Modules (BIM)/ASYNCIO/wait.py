import asyncio

#asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)

"""
Waiting  Primitives:

** aws=awaitables; loop is deprecated; timeout max sec(s) before return; **

Return When:
1.) FIRST_COMPLETED
The function will return when any future finishes or is cancelled.

2.) FIRST_EXCEPTION
The function will return when any future finishes by raising an exception.
**If no future raises an exception then it is equivalent to ALL_COMPLETED.

3.) ALL_COMPLETED
The function will return when all futures finish or are cancelled.
"""
async def main():
    async def foo():
        return 42

    task = asyncio.create_task(foo())
    done, pending = await asyncio.wait({task})

    if task in done:
        print("all done")

asyncio.run(main())
