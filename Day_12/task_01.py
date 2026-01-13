class user:
    def __init__(self, username):
        self.username = username
        self.is_active = True
user = user("Sanjid Hasan")
print(f"""User: {user.username} 
Active: {user.is_active}""")
