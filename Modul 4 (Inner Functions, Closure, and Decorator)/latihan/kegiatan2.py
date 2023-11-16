# Penerapan single decorators to single functions
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'Hello There'

# say_hi()
print(say_hi())