import asyncio

"""

cancelled()
Return True if the Task is cancelled.

done()
Return True if the Task is done.

result()
Return the result of the Task.

    If the Task is done, the result of the wrapped coroutine is returned (or if the coroutine raised an exception, that exception is re-raised.)

    If the Task has been cancelled, this method raises a CancelledError exception.

    If the Task’s result isn’t yet available, this method raises a InvalidStateError exception.

exception()
Return the exception of the Task.

    If the wrapped coroutine raised an exception that exception is returned. If the wrapped coroutine returned normally this method returns None.

    If the Task has been cancelled, this method raises a CancelledError exception.

    If the Task isn’t done yet, this method raises an InvalidStateError exception.

add_done_callback(callback, *, context=None)
Add a callback to be run when the Task is done.

    This method should only be used in low-level callback-based code.


remove_done_callback(callback)
Remove callback from the callbacks list.

    This method should only be used in low-level callback-based code.


get_stack(*, limit=None)
Return the list of stack frames for this Task.

    If the wrapped coroutine is not done, this returns the stack where it is suspended.
    If the coroutine has completed successfully or was cancelled, this returns an empty list.
    If the coroutine was terminated by an exception, this returns the list of traceback frames.

    **The frames are always ordered from oldest to newest.

    **Only one stack frame is returned for a suspended coroutine.

The optional limit argument sets the maximum number of frames to return; by default all available frames are returned.

The ordering of the returned list differs depending on whether a stack or a traceback is returned:

    the newest frames of a stack are returned, but the oldest frames of a traceback are returned. (This matches the behavior of the traceback module.)

print_stack(*, limit=None, file=None)
Print the stack or traceback for this Task.

    This produces output similar to that of the traceback module for the frames retrieved by get_stack().

    The limit argument is passed to get_stack() directly.

    The file argument is an I/O stream to which the output is written; by default output is written to sys.stderr.

get_coro()
Return the coroutine object wrapped by the Task.

New in version 3.8.

get_name()
Return the name of the Task.

    If no name has been explicitly assigned to the Task, the default asyncio Task implementation generates a default name during instantiation.

    New in version 3.8.

set_name(value)
Set the name of the Task.

    The value argument can be any object, which is then converted to a string.

    In the default Task implementation, the name will be visible in the repr() output of a task object.

    New in version 3.8.

"""
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())
