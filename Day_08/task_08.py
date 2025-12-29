import random
def sort_list(x = []):
    
    import time
    start = time.time()
    x = sorted(x)
    end = time.time()
    print(f"Sorting took: {end - start} seconds")

x = [random.randint(0, 10000) for _ in range(1000)]

sort_list(x)
