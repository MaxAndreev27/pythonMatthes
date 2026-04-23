# Decorator example
def printlog(func):
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg + 2)

    return wrapper


# Universal decorator for any function with 0..N arguments
def universal_printlog(func):
    def wrapper(*args, **kwargs):
        print("Inside decorator CALLING: " + func.__name__)
        return func(*args, **kwargs)

    return wrapper


@universal_printlog
def foo(x, y):
    print(f"Inside foo: {x + y}")


foo(3, 5)


@universal_printlog
def zero_arg_func():
    print("Func with 0 arguments")


zero_arg_func()


# Decorator for function with >=1 argument, good for class methods
def universal_printlog_for_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Inside decorator_self CALLING: {func.__name__}")
        return func(self, *args, **kwargs)

    return wrapper


@universal_printlog_for_method
def bar(x):
    print(f"Inside bar: {x}")


bar(1)


# Use decorator with self only for class method
class Invoice:
    def __init__(self, id_number, total):
        self.id_number = id_number
        self.total = total
        self.owed = total

    @universal_printlog_for_method
    def record_payment(self, amount):
        self.owed -= amount


inv = Invoice(42, 2000)
inv.record_payment(150)
print(f"Total: {inv.total}, Owned: {inv.owed}")


# Decorator with parameter
def add(increment):
    def decorator(func):
        def wrapper(n):
            return func(n) + increment

        return wrapper

    return decorator


@add(4)
def f(n):
    return n


print(f"Function with add decorator: {f(3)}")

# You also use like this:
add2 = add(2)
# @add2


# Class Decorator
class Printlog:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"CALLING: {self.func.__name__}")
        return self.func(*args, **kwargs)


@Printlog
def baz(x, y):
    print(f"Inside baz: {x + y}")


baz(3, 5)


class Add:
    def __init__(self, increment):
        self.increment = increment

    def __call__(self, func):
        def wrapper(n):
            return func(n) + self.increment

        return wrapper


@Add(6)
def fc(n):
    return n


print(f"Function with add decorator: {fc(3)}")
