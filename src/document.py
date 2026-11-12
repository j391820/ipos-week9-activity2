from random import randint
import aiohttp


class Document:
    def __init__(self, name, body):
        self.name = name
        self.body = body


    @staticmethod
    async def get_json():
        """
        Queries remote API for a random social media comment object.

        Args:
            None.

        Returns:
            Comment as a JSON.
        """
        async with aiohttp.ClientSession() as session:
            post_id = randint(1, 500)
            url = f"https://jsonplaceholder.typicode.com/comments/{post_id}"
            async with session.get(url) as resp:
                data = await resp.json()
        return data
    
    @staticmethod
    async def get_body():
        """
        Extracts body from comment object.

        Args:
            None.

        Returns:
            The body of the comment.
        """
        content = await Document.get_json()
        return content['body']

    @classmethod
    async def create(cls, name):
        """
        Creates a new document object of supplied name and with random content.

        Args:
            name(string): document name..

        Returns:
            New document object.
        """
        body = await cls.get_body()
        return cls(name, body)









