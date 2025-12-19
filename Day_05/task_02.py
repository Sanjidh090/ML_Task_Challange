user = { 'id': 1}
email = user.get('email')
print(email)  
message = user.get('email', 'Email not provided')
print(message)