import random
x = [random.randint(0, 10000) for _ in range(1000)]
def sort_list(x = []):
    import time
    start = time.time()
    x = sorted(x)
    end = time.time()
    print(f"Sorting took: {end - start} seconds")
if __name__ == "__main__": 
    sort_list(x)

