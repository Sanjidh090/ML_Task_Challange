class User:
    def __init__(self, username):
        self.username = username
    def info(self):
        return f"{self.username} is Added in user information."
        
class Admin(User):
    def __init__(self, username, Access):
        super().__init__(username)
        self.access = Access     
    def delete_db(self):
        return f"Admin {self.username} deleted the database and has access to {self.access}!"

user = User("Sanjid")
print(user.info())                    

admin = Admin("Hasan", True)
print(admin.delete_db())                
print(admin.username)                      
print(admin.access)                    
