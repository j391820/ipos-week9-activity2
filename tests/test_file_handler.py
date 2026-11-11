import unittest
from src.document import Document
from src.file_handler import save_document, upload_document
from pathlib import Path


class TestFileHandler(unittest.IsolatedAsyncioTestCase):
    """
    Unit tests for File Handler functionalities including saving file to disk
    and uploading to "remote server".
    """
    
    async def asyncSetUp(self):
        """
        Set up the test environment by creating a test document.
        """
        # Create a test document
        self.document_object = await Document.create("test.txt")

        # Get the path of the created file
        self.target_path = Path("local/test.txt")

    async def asyncTearDown(self):
        """
        Clean up the test environment by removing test document.
        """
        for path in [Path("local/test.txt"), Path("remote/test.txt")]:
            if path.is_file():
                path.unlink()

    async def test_save_document(self):
        """
        Tests that created file is saved to disk.
        """
        # Save file to disk
        save_document(self.document_object)

        self.assertTrue(
            self.target_path.is_file(),
            msg=f"The document was not written to disk at {self.target_path}",
        )

    async def test_upload_document(self):
        """
        Tests that file is transfered to "remote" directory.
        """
        save_document(self.document_object)
        upload_document(self.document_object.name)
        destination_path = Path("remote/test.txt")

        self.assertTrue(
            destination_path.is_file(),
            msg=f"The document was not uploaded to {destination_path}",
        )

    async def test_upload_document_removed_locally(self):
        """
        Tests that file is removed from local directory.
        """
        save_document(self.document_object)
        upload_document(self.document_object.name)

        self.assertFalse(
            self.target_path.is_file(),
            msg=f"The document should have been deleted, but it still exists at {self.target_path}",
        )


if __name__ == "__main__":
    unittest.main()
