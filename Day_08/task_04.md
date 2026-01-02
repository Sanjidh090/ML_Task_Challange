# Task 04 : The Queue Bottleneck
```Goal:``` Compare ```list.pop()``` vs ```list.pop(0)```.
</br> ```Deep Dive:``` .pop() removes the last item (O(1)).
</br>```.pop(0)```  removes the first item, requiring a Left Shift of all remaining items to fill the gap (O(N)). 
</br>```Fix:``` Use collections.deque for fast ```First-In-First-Out``` queues.

This part in the code solves the first part.
```python
import time

list = [i for i in range(-50000000, 5000000)]
start = time.time()
list.pop(0)
end = time.time()
```
Here is the part for ```pop()```
```python
start = time.time()
list.pop()
end = time.time()
time_pop = end - start
print(f"Time taken {time_pop:.6f} seconds for pop()")
```
Running the code several times with varying range will show the time comparison
