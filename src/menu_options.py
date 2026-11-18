from src.event_notifier import Publisher, Subscriber, SubscriptionPersist
import src.create_users as Users
from src.create_users import UsersPersist
from src.document import Document as document_creator
from src.file_handler import save_document, upload_document
from pathlib import Path
import time


user_factory = Users
publisher = Publisher()
user_persistent_data = UsersPersist("users.json")
users = user_persistent_data.load_from_json()
subscription_persistent_data = SubscriptionPersist("subscriptions.json")
publisher.subscribers = subscription_persistent_data.load_from_json(users)


def login():
    print("Please select a user to login:")
    count = 0
    for user in users:
        print(f"{count}. {user.name}")
        count += 1
    current_user = users[int(input("User selection: "))]
    print(f"Welcome {current_user.name}")
    print()
    time.sleep(1)
    return current_user


current_user = login()


def handle_new_user():
    name = input("Name: ")
    print("Select a role:")
    print("Admin")
    print("Editor")
    print("Viewer")
    user_choice = input("User selection: ")
    new_user = user_factory.create_user(user_choice.lower(), name)
    users.append(new_user)


def handle_print_users():
    for user in users:
        print(f"{user.name}: {type(user).__name__}")
    time.sleep(1)


def handle_subscribe_user():
    print("Please select a user:")
    count = 0
    for user in users:
        print(f"{count}. {user.name}")
        count += 1
    user_choice = int(input("User selection: "))
    new_subscriber = Subscriber(users[user_choice])
    publisher.register(new_subscriber)


async def handle_document_creation():
    document_name = input("Please enter a name: ")
    created_document = await document_creator.create(document_name)
    save_document(created_document)


def handle_document_upload():
    count = 0
    directory = Path("./local")
    files = []
    for item in directory.iterdir():
        files.append(item)
    for file in files:
        print(f"{count}: {file.name}")
        count += 1
    user_selection = int(input("please select a file: "))
    upload_document(files[user_selection].name)
    publisher.notify(
        f"User {current_user.name} uploaded {files[user_selection].name} to the cloud")
    time.sleep(2)


def save_state():
    subscription_persistent_data.save_to_json(publisher.subscribers)
    user_persistent_data.save_to_json(users)
