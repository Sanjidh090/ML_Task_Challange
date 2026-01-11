USER = "admin"

def admin_required(func):
    def wrap(*args, **kwargs):
        if USER != "admin":
            raise PermissionError("Admin required!")
        return func(*args, **kwargs)
    return wrap

@admin_required
def delete_user(user_id):
    print(f"User {user_id} has been deleted.")

delete_user(1)
