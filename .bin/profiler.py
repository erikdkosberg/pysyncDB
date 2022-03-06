# A simple class to check function calls on a block of code
class Profile():
    def __init__(self, code):
        import cProfile
        cProfile.run(statement=code)


expr1 = "[z**2 for z in range(1000000)]"
expr2 = "(z**2 for z in range(1000000))"

Profile(repr(expr1))
Profile(repr(expr2))

import sys

print(sys.getsizeof(expr1))
print(sys.getsizeof(expr2))


