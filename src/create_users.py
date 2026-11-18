import json
from pathlib import Path


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
        raise ValueError(
            "Invalid user type entered. Acceptable values are admin, editor, viewer.")

        # # Alt version where the program does not stop if error occurs:
        # print("Invalid user type")
        # return None


class UsersPersist:
    """
    Class with functions to save and load users to a json file.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_from_json(self):
        """
        Loads users from json file.

        Args:
            None.

        Returns:
            users (list): list of users.

        Side Effects:
            Saves a json file to the drive.
        """
        users = []
        # if file doesn't exist create with empty list.
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")
        else:
            with open(self.file_path, "r") as file:
                user_data = json.load(file)
            for data in user_data:
                # recreate user objects.
                existing_user = create_user(data["role"], data["name"])
                # append to list of users.
                users.append(existing_user)
        return users

    def save_to_json(self, users):
        """
        Saves users to json file.

        Args:
            users (list): list of users.

        Returns:
            None.

        Side Effects:
            Saves a json file to the drive.
        """
        my_list = []
        for user in users:
            # append each user to list as a dictionary.
            my_list.append(
                {
                    "name": user.name,
                    "role": type(user).__name__
                }
            )
        with open(self.file_path, "w") as file:
            json.dump(my_list, file, indent=4)
