import asyncio

# Create a coroutine
coro = asyncio.sleep(1, result=3)
    
# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, asyncio.loop())

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3

"""
If an exception is raised in the coroutine, the returned Future will be notified.

It can also be used to cancel the task in the event loop:

"""

try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')

asyncio.run(main())
