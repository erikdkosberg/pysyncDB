"""
 ________
|For Loops:
|[*] A way to iterate through an iterable object such as a list, dict, etc.
|[*] In general, a for loop is used when looping through a pre-defined range of objects
|[*]

"""
# Basic Syntax
for x in range(10):
    pass

# Looping through a list
test_ls = [1, 2, 3]
for x in test_ls:
    pass

# Looping through a dict
test_dict = {"data1": 1, 1: 2}

print(test_dict)
key = "data1"
for k, v in test_dict:
    if k == key:
        print(v)


# Putting it into a function

def for_func(ls):
    for k, v in ls:
        if k == key:
            pass
