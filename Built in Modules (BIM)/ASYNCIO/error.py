

#Error Handling
"""
Allows customizing how exceptions are handled in the event loop.

loop.set_exception_handler(handler)
Set handler as the new event loop exception handler.
    If handler is None, the default exception handler will be set.
    Otherwise, handler must be a callable with the signature matching (loop, context),
    where loop is a reference to the active event loop, and context is a dict object
    containing the details of the exception (see call_exception_handler() documentation
                                             for details about context).

loop.get_exception_handler()
    Return the current exception handler, or None if no custom exception handler was set.

    New in version 3.5.2.

loop.default_exception_handler(context)
Default exception handler.

    This is called when an exception occurs and no exception handler is set.
    This can be called by a custom exception handler that wants to defer to the default handler behavior.
    context parameter has the same meaning as in call_exception_handler().

loop.call_exception_handler(context)
Call the current event loop exception handler.

context is a dict object containing the following keys (new keys may be introduced in future Python versions):
    ‘message’: Error message;
    ‘exception’ (optional): Exception object;
    ‘future’ (optional): asyncio.Future instance;
    ‘handle’ (optional): asyncio.Handle instance;
    ‘protocol’ (optional): Protocol instance;
    ‘transport’ (optional): Transport instance;
    ‘socket’ (optional): socket.socket instance.
    **Note This method should not be overloaded in subclassed event loops.
    **For custom exception handling, use the set_exception_handler() method.
"""
#DEBUGGING
"""
loop.get_debug()
Get the debug mode (bool) of the event loop.
    The default value is True if the environment variable PYTHONASYNCIODEBUG is set to a non-empty string, False otherwise.

loop.set_debug(enabled: bool)
Set the debug mode of the event loop.
    Changed in version 3.7: The new Python Development Mode can now also be used to enable the debug mode.
