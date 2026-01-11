def repeat_factory(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func()
        return wrapper
    return decorator
@repeat_factory(3)
def process():
    print("Processing...")

process()
