import time

N = 1_000_000
data_list = list(range(N))

def create_dict(N):
    start_time = time.time()
    data_dict = {}
    for item in data_list:
        data_dict[item] = item
    end_time = time.time()
    print("Time" \
    " to build dictionary:", end_time - start_time, "seconds")
    return data_dict

data_dict = create_dict(N)

def search_dict(data_dict, N):
    search_key = N - 1

    start_time = time.time()
    value = data_dict[search_key]
    end_time = time.time()

    print("Time to search in dictionary:", end_time - start_time, "seconds")

search_dict(data_dict, N)
