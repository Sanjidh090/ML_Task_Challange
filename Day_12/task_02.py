class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} here.")

# Create an instance
current_user = User("Sanjid")
new_user = User("Hasan")

# Calling the method
current_user.login()
new_user.login()
