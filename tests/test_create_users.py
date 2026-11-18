from src.create_users import UsersPersist, create_user
import unittest
from pathlib import Path


class TestCreateUsers(unittest.TestCase):
    """
    Unit tests for create user module.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # set up a test document and directory
        self.file_path = Path("./files/test.json")
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        # initialise UserPersists class from module
        self.users_persist = UsersPersist(self.file_path)
        # create a new test user
        self.user = create_user("admin", "Bob")
        self.users = [self.user]

    def tearDown(self):
        """
        Clean up the test environment by removing test document and path.
        """
        if self.file_path.is_file():
            self.file_path.unlink()
            self.file_path.parent.rmdir()

    def test_save_to_json_create_file(self):
        """
        Tests that created file is saved to disk.
        """
        self.users_persist.save_to_json(self.users)

        self.assertTrue(
            self.file_path .is_file(),
            msg=f"The document was not written to disk at {self.file_path}",
        )

    def test_load_from_json(self):
        """
        Tests whether can read user back from saved file.
        """
        self.users_persist.save_to_json(self.users)
        users = self.users_persist.load_from_json()

        self.assertEqual(len(users), 1)
