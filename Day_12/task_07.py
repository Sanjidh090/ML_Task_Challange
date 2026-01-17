class User:
    def __init__(self, username):
        self.username = username
    def info(self):
        return f"{self.username} is Added Here"   
      
class Admin(User):
    def __init__(self, username):
        super().__init__(username)
    def delete_all(self):
        return f"Admin {self.username} deleted "

user = User("Sanjid")
print(user.info())                    
admin = Admin("Hasan")
print(admin.delete_all())         
