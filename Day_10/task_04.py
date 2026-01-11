def deco(func):
    def wrap(*args):
        print("Args:", args)
        
    return wrap

@deco
def add(a, b):
    return a + b

print(add(2, 3))
