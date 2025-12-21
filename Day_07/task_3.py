try:
    x = 10
    y = 0
    print("Result:", x / y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")