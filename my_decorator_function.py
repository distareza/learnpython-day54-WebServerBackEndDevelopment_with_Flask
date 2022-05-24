"""
    Decorator Function is a function which wrap another function and give another functionality or modify a functionality before or after
"""

def my_decorator(function):
    def wrapper_function():
        print("start decorator")
        # Dosomethingbefore
        function()
        # Dosomethingafter
        print("final decorator")
    return wrapper_function

@my_decorator
def test_print():
    print("hello world")

test_print()
"""
output :
    start decorator
    hello world
    final decorator
"""