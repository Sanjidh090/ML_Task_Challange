import time
import random

a = [random.randint(-1, 1000000) for i in range(-1, 1000000)]
start = time.perf_counter()
if '-1' in a:
    print("Found -1 in the list")
else:
    print("-1 not found in the list")
     # Simulate some work being done
end = time.perf_counter()
elapsed = end - start
print(f"Execution time for a list : {elapsed:.4f} seconds")
print("==" * 40)
print("Now testing with a set")
start = time.perf_counter()
a = {random.randint(-1, 1000000) for i in range(-1, 1000000)}
start = time.perf_counter()
if '-1' in a:
    print("Found -1 in the set")
else:
    print("-1 not found in the set")
end = time.perf_counter()
elapsed = end - start
print(f"Execution time for a set : {elapsed:.4f} seconds")