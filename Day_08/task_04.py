import time

list = [i for i in range(-50000000, 5000000)]
start = time.time()
list.pop(0)
end = time.time()
time_list = end - start
print(f"Time taken {time_list:.6f} seconds for pop(0)")

start = time.time()
list.pop()
end = time.time()
time_pop = end - start
print(f"Time taken {time_pop:.6f} seconds for pop()")
