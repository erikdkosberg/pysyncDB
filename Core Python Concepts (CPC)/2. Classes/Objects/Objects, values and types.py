# Every object has an identity, a type and a value
"""
An objects identity never changes once its been created;
    essentially it is the objects address in memory.

-'is' operator compares the identity of two objects
-id() function returns an integer identity representation

An object's type determines the supported operations;
    also defines the possible values and is unchangeable

-type() function returns an object's type

The value of an object can change or it can never change;
    mutable objects can change their values
    immutable one's can't (it's actually more subtle)
        an immutable object could contain
        references to mutable objects whose values can change

Garbage collection refers to unreachable objects

Catching an exception with try/except may keep objects alive

Objects can contain references to external resources;
    i.e. open files or windows
    since garbage collection isn't guaranteed,
    you can usually close them with close()

try/finally and with provide good ways to do this

Objects containing references to other objects
    are known as containers.

    -i.e. tuples, lists, dictionaries
    -if immutable container refers to mutable object:
        its value changes if that mutable object changes

Types affect almost all aspects of object behavior.

Even the importance of object identity
    is affected in some sense:
        for immutable types,
        operations that compute new values may actually
        return a reference to any existing object with the
        same type and value, while for mutable objects this
        is not allowed.

    E.g., after a = 1; b = 1,
     a and b may or may not refer to the same object
      with the value one,

    depending on the implementation,
     but after c = []; d = [],
        c and d are guaranteed to refer to two different,
        unique, newly created empty lists.

    (Note that c = d = [] assigns the same object to both c
     and d.)
"""