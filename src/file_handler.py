from document import Document
import shutil


def save_document(document):
    file_path = f"../local/{document.name}"
    with open (file_path, "w") as file:
        file.write(document.body)



