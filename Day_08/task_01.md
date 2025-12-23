## Task 01 :
linear scan or linear search in python goes with the size vs time. If the list is long, time for scan will be long ,too .
Time complexity : O(N)

```python
import time
list = [i for i in range(-5000000, 5000000)]   
start = time.perf_counter()
for i in range(len(list)):
    if list[i] == -5:
        print(f" -5 found at index {i}")
        break
end = time.perf_counter()
elapsed = end - start
print(f"Execution time for search elapsed: {elapsed:.4f} seconds")
```

in this code, if we change the range , increase it a little bit, time goes up as we increast the length and vice versa, the shorter the list, the less time it takes.

![alt text](image.png)