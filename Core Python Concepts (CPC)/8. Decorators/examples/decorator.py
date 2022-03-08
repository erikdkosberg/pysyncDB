def my_function():

    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.

description = my_function

# Accessing the function from the variable I assigned it to.

print(description())

def outer_function():

    def inner_function():

        print('I came from the inner function.')

    # Executing the inner function inside the outer function.
    inner_function()

outer_function()

def outer_function():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()

homework()


#  A function can be passed to another function as an argument.

def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')

# Calling the friendly_reminder function with the action function used as an argument.

friendly_reminder(action)