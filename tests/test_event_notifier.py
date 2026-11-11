import unittest
from unittest.mock import patch
from src.event_notifier import Publisher, Subscriber


class TestEventNotifier(unittest.TestCase):
    """
    Unit tests for Event Notifier functionalities including adding and
    removing subscriber, as well as notifying the subscribers.
    """

    def setUp(self):
        """
        Set up the test environment by initializing publisher and subscriber
        classes.
        Creating a "user".
        """
        self.publisher = Publisher()
        self.user = "Bob"
        self.subscriber = Subscriber(self.user)

    def test_add_subscriber(self):
        """
        Test adding a subscriber actually adds it to the list of subscribers.
        """
        self.publisher.register(self.user)
        self.assertIn(self.user, self.publisher.subscribers)

    def test_remove_subscriber(self):
        """
        Test removing a subscriber actually removes it from the list of
        subscribers.
        """
        self.publisher.register(self.user)
        self.publisher.unregister(self.user)
        self.assertNotIn(self.user, self.publisher.subscribers)

    @patch('builtins.print')
    def test_user_notified(self, mock_print):
        """
        Test subscribers actually receive the message.
        """
        self.publisher.register(self.subscriber)
        self.publisher.notify("my message")

        mock_print.assert_called_with("Bob received: my message")


if __name__ == "__main__":
    unittest.main()
