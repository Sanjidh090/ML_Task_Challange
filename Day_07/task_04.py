try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("No negetives.")
    print(f"You entered: {num}")
except ValueError :
    print("Invalid input")