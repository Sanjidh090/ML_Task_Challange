import functools

def my_decorator(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def calculate_tax(amount):
    return amount * 0.1

print(calculate_tax(1000))
print(calculate_tax.__name__) 
print(calculate_tax.__doc__)
