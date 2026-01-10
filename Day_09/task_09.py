def injection():
    while True:
        # Receive the value
        x = yield 
        if x == "SHUTDOWN":
            print("Shutting down...")
            break
            
        if x == "REBOOT":
            print("Rebooting...")
            continue
            
        # Only process if it's not a control signal
        print(f"Processing: {x}")

# Execution
c = injection()
next(c)  # Prime the coroutine
c.send("REBOOT")
c.send("Task 1")
try:
    c.send("SHUTDOWN")
except StopIteration:
    pass
