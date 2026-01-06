# Task 08
```python
import random
a = [random.randint(0, 100) for _ in range(51)]
b = [random.randint(0, 100) for _ in range(51)]
```
a & b are two list with random numbers.
```match_lists(a,b)``` is the function which uses two for loops to check if elements of lists matches and ```count``` variable returns how many times ````matches``` were found.

```python
def match_lists(a =[], b = []):
    match = []
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            count += 1
            if a[i] == b[j]:
                match.append(a[i])
```
Here is the rest of the function for better understanding.
```python
    print(match)   
    print(set(match))         
    print(f"Number of matching elements: {len(match)}") 
    print(f"Total comparisons made: {count}") 
```

```match_lists(a, b)``` This part calls the function and executes and see how many elements match in those lists.
