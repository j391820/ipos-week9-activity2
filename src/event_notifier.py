class Publisher:
    """
    Class to represent an event publisher.
    """

    def __init__(self):
        # list to hold all the subscribers.
        # if expanding system could implement different lists for different even types.
        self.subscribers = []

    def register(self, user):
        """
        Register user to subscribers.

        Args:
            user (string): Username to register.

        Returns:
            None.

        Side effect:
            Add username to the list of subscribers.
        """
        self.subscribers.append(user)

    def unregister(self, user):
        """
        Unregister user to subscribers.

        Args:
            user (string): Username to register.

        Returns:
            None.

        Side effect:
            Remove username from the list of subscribers.
        """
        self.subscribers.remove(user)

    def notify(self, message):
        """
        Notify all suscribed users.

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

    def __init__(self, name):
        self.name = name

    def receive(self, message):
        """
        User recieves the message.

        Args:
            message (string): Message to send to the user.

        Returns:
            None.

        Side effect:
            None.
        """
        print(message)
