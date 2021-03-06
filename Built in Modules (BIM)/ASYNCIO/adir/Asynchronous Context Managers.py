from logging import log


class AsyncContextManager:
    async def __aenter__(self):
        await log("entering context")

    async def __aexit__(self, exc_type, exc, tb):
        await log("exiting context")