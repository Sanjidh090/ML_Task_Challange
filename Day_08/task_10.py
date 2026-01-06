import time
x = [1,2,5,6,8,9,7,10,4,5]
pos = 4
def slice_list(source,k):
    s = time.time()
    new_list = []
    for i in range(0,k):
        new_list.append(source[i])
    e = time.time()
    print(f"Time taken: {e - s} seconds")
    return new_list

print(slice_list(x,pos))  # [1, 2, 3]
