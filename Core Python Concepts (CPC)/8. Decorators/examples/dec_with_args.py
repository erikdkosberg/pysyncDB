"""
*args will take an unlimited number of arguments of any type,
    such as 10, True, or 'Brandon'.
**kwargs will take an unlimited number of keyword arguments,
    such as count=99, is_authenticated=True, or name='Brandon'.

"""

def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Example docstring for function'''

    pass
"""
Decorators hide the function they are decorating.
If I check the __name__ or __doc__ method we get an unexpected result.
"""

print(my_func.__name__)
print(my_func.__doc__)

# To fix this issue I will use functools.
# Functools wraps will update the decorator with the decorated functions attributes.

from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    pass

print(my_func.__name__)
print(my_func.__doc__)