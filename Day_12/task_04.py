class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private (name-mangled)

    def check_password(self, password):
        return self.__password == password
        
user = User("sanjid", "1234")

print(user.username)
# sanjid

print(user.check_password("1234"))
# True 
