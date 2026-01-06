# Task 07
We created a list with random numbers
```python
import random
x = [random.randint(0, 10000) for _ in range(1000)]
```
Here is the function that sorts our list into ordered format.
```python
def sort_list(x = []):
    import time
    start = time.time()
    x = sorted(x)
    end = time.time()
    print(f"Sorting took: {end - start} seconds")
```
We used python's pre-built ```sorted()``` method here.
And, Finally, ```sort_list(x)``` provides the desired output.
