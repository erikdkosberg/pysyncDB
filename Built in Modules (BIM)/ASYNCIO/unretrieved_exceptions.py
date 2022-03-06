import asyncio

async def

async def bug():
    raise Exception("Dang")

async def main():
    asyncio.create_task(bug())

asyncio.run(main(), debug=True)
