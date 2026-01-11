def wrapper(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

def old_func():
    print("Hello")

new_func = wrapper(old_func)
new_func()
