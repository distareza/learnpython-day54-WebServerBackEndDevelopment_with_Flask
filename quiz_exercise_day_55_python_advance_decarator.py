"""
Instructions
Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given
and finally the returned output.

Expected Output
https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd

HINT 1: You can use function.__name__ to get the name of the function.

HINT 2: You'll need to use *args

"""
# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args, **kargs):
        arg1 = args[0]
        arg2 = args[1]
        arg3 = args[2]
        print(f"You called {func.__name__}{args}")
        print(f"It return {func(arg1, arg2, arg3)}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a:int, b:int, c:int):
    return a*b*c

a_function(1,2,3)