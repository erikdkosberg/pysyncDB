import asyncio
"""
Class asyncio.Server
Server objects are asynchronous context managers. When used in an async with statement,
it’s guaranteed that the Server object is closed and not accepting new connections when
the async with statement is completed:

    srv = await loop.create_server(...)

    async with srv:
        # some code

# At this point, srv is closed and no longer accepts new connections.
Changed in version 3.7: Server object is an asynchronous context manager since Python 3.7.

close()
Stop serving: close listening sockets and set the sockets attribute to None.
    The sockets that represent existing incoming client connections are left open.
    The server is closed asynchronously, use the wait_closed() coroutine to wait until the server is closed.

get_loop()
Return the event loop associated with the server object.
    New in version 3.7.

coroutine start_serving()
Start accepting connections.

    This method is idempotent, so it can be called when the server is already being serving.
    The start_serving keyword-only parameter to loop.create_server() and asyncio.start_server() allows creating a Server
        object that is not accepting connections initially.
    In this case Server.start_serving(), or Server.serve_forever() can be used to make the Server start accepting connections.
    New in version 3.7.

coroutine serve_forever()
Start accepting connections until the coroutine is cancelled. Cancellation of serve_forever task causes the server to be closed.

This method can be called if the server is already accepting connections. Only one serve_forever task can exist per one Server object.

Example:

    async def client_connected(reader, writer):
        # Communicate with the client with
        # reader/writer streams.  For example:
        await reader.readline()

    async def main(host, port):
        srv = await asyncio.start_server(
            client_connected, host, port)
        await srv.serve_forever()

    asyncio.run(main('127.0.0.1', 0))
    New in version 3.7.

is_serving()
Return True if the server is accepting new connections.
    New in version 3.7.

coroutine wait_closed()
Wait until the close() method completes.

sockets
List of socket.socket objects the server is listening on.
    Changed in version 3.7: Prior to Python 3.7 Server.sockets used to return an internal list of server sockets directly. In 3.7 a copy of that list is returned.

"""
async def client_connected(reader, writer):
    # Communicate with the client with
    # reader/writer streams.  For example:
    await reader.readline()

async def main(host, port):
    srv = await asyncio.start_server(
        client_connected, host, port)
    await srv.serve_forever()

asyncio.run(main('127.0.0.1', 0))
