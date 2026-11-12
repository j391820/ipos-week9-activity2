import json
from pathlib import Path


class Publisher:
    """
    Class to represent an event publisher.
    """

    def __init__(self):
        # list to hold all the subscribers.
        # if expanding system could implement different lists for different
        # even types.
        self.subscribers = []

    def register(self, subscriber):
        """
        Register user to subscribers.

        Args:
            Subscriber (subscriber object): Subscriber to register.

        Returns:
            None.

        Side effect:
            Add subscriber to the list of subscribers.
        """
        self.subscribers.append(subscriber)

    def unregister(self, subscriber):
        """
        Unregister subscriber from subscribers.

        Args:
            Subscriber (subscriber object): Subscriber to unregister.

        Returns:
            None.

        Side effect:
            Remove username from the list of subscribers.
        """
        self.subscribers.remove(subscriber)

    def notify(self, message):
        """
        Notify all subscribed users.

        Args:
            message (string): Message to send to users.

        Returns:
            None.

        Side effect:
            None.
        """
        for subscriber in self.subscribers:
            subscriber.receive(message)


class Subscriber:
    """
    Class to represent an subscriber.
    """

    def __init__(self, user):
        self.user = user

    def receive(self, message):
        """
        User receives the message.

        Args:
            message (string): Message to send to the user.

        Returns:
            None.

        Side effect:
            None.
        """
        print(f"{self.user.name} received: {message}")


class SubscriptionPersist:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_from_json(self, users):
        subscribers = []
        # if file doesn't exist create with empty list.
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")
            return subscribers
        else:
            with open(self.file_path, "r") as file:
                names = json.load(file)
            # if subscribers or users file is just empty list stop.
            if len(names) == 0 or len(users) == 0:
                return subscribers 
            else:
                # loop through file.
                for name in names:
                    for user in users:
                        # map names in subscribers to names in users file.
                        if name == user.name:
                            # recreate subscriber objects from user objects.
                            existing_subscriber = Subscriber(user)
                            # append to list of subscribers.
                            subscribers.append(existing_subscriber)
                return subscribers

    def save_to_json(self, subscriptions):
        my_list = []
        for subscriber in subscriptions:
            my_list.append(subscriber.user.name)
        with open(self.file_path, "w") as file:
            json.dump(my_list, file, indent=4)
