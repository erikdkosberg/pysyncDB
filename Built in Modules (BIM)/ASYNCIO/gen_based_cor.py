import asyncio

#DEPRECATED 3.8+

@asyncio.coroutine
def old_style_coroutine():
    yield from asyncio.sleep(1)

async def main():
    await old_style_coroutine()

asyncio.run(main())
