import asyncio

"""

If it is desired to completely ignore cancellation (not recommended):

    the shield() function should be combined with a try/except clause

try:
    res = await shield(something())
except CancelledError:
    res = None

"""
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 1),
        factorial("B", 2),
        factorial("C", 3),
    )

asyncio.run(main())
