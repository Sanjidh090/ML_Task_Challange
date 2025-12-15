user = None 
if user != None and user.role == 'admin' : 
    print(f"User is {user} and user's role is {user.role}")
else: 
    print("User is None or does not have admin access")
