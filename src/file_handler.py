from src.document import Document
import shutil


def save_document(document):
    """
    Saves a document object to the drive.

    Args:
        document (document object): Document object to save.

    Returns:
        None.

    Side Effects:
        - Saves a document object to the drive.
    """
    file_path = f"local/{document.name}"
    with open (file_path, "w") as file:
        file.write(document.body)

def upload_document(filename):
    """
    Simulates uploading a file to a remote server.

    Args:
        filename (string): Name of the file to upload.

    Returns:
        None.

    Side Effects:
        - Moves file from local to remote.
    """    
    source = f"local/{filename}"
    destination = f"remote/{filename}"
    shutil.move(source, destination)

