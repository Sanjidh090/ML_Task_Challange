def gen():
    yield 1
    yield 2
g = gen()
try:
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print("No more values to yield.")
    g = gen()  # Reinitialize the generator
    print(next(g))
