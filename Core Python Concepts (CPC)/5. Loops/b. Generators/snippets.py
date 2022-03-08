"""
 ___________
|Generators:|
|[*] A special kind of function that returns an iterator.
|[*] Doesn't store its contents into memory.
|[*] Allows you to delay the evaluation of an expression until needed.

A generator object can be created with either a yield statement/expression inside
of a function or using () instead of [] via generator comprehension

The object itself can be infinitely large, yet we can still iterate through it

"""
file = "_data_.csv"

#Generators using Yield
def reader(file):
    for row in open(file, 'r'):
        yield row

def infinite():
    n = 0
    while True:
        yield n
        n += 1

def multi_yield():
    y1 = "test1"
    yield y1
    y2 = "test2"
    yield y2

gen = infinite()
print(next(gen))
print(next(gen))

"""
for i in infinite():
    print(i)
"""

#Generator Comprehension
gen = (row for row in open(file))

#Generator Error Handling
ls = ['a', 'b', 'c']
it = iter(ls)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

#Generator Performance
import sys
import cProfile

n = [i ** 2 for i in range(10000)]
n2 = (i ** 2 for i in range(10000))

print("With list comprehension: " + str((sys.getsizeof(n))) + " bytes")
print("With gen comprehension: " + str((sys.getsizeof(n2))) + " bytes")

cProfile.run('sum((i*2 for i in range(10000)))')
cProfile.run('sum([i*2 for i in range(10000)])')

#.send() -> when using yield expression rather than statement, send value back to gen to be picked up after execution
#.throw() -> allows you to throw exceptions with the generator
#.close() -> allows you to stop a generator raises StopIteration, an exception which signals the end of finite iterator

"""
#example csv parsing

list_line = (s.strip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
"""