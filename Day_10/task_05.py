import time
def timer(func):
    def wrapper():
        print(f"Function is running...")
        func()
        print(f"Function finished running.")     
    return wrapper
@timer
def my_function():
    print(f"Time is {time.time()}")

my_function()
