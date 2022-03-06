def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func

@my_decorator_func
def my_func():
    pass
