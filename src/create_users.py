class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        user_string = super().__str__()
        return f"{user_string}, User Type: Admin"

class Editor(User):
    def __init__(self, name):
        super().__init__(name)

class Viewer(User):
    def __init__(self, name):
        super().__init__(name)


def create_user(user_type, name):
    if user_type.lower() == "admin":
        return Admin(name)
    elif user_type.lower() == "editor":
        return Editor(name)
    elif user_type.lower() == "viewer":
        return Viewer(name)
    else:
        raise ValueError("Invalid user type entered. Acceptable values are admin, editor, viewer.")

        # # Alt version where the program does not stop if error occurs:
        # print("Invalid user type")
        # return None

user1 = create_user("admin", "Stanley")
print(Admin(user1.name))
print(Admin(user1))
print(User(user1.name))