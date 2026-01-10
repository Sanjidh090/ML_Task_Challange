def square(x):
    yield x * x

def filter_even(numbers):
    for number in numbers:  # iterate over the input
        if number % 2 == 0:
            yield number
filtered_numbers = filter_even(square(6))
for i in filtered_numbers:
    print(i)
