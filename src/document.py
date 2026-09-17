from random import randint
import aiohttp
import asyncio

class Document:
    def __init__(self, name, body):
        self.name = name
        self.body = body

    @staticmethod
    async def get_json():
        async with aiohttp.ClientSession() as session:
            post_id = randint(1, 500)
            url = f"https://jsonplaceholder.typicode.com/comments/{post_id}"
            async with session.get(url) as resp:
                data = await resp.json()
        return data
    
    @staticmethod
    async def get_body():
        content = await Document.get_json()
        return content['body']

    @classmethod
    async def create(cls, name):
        body = await cls.get_body()
        return cls(name, body)







my_doc = asyncio.run(Document.create("test.txt"))
print(f"Document {my_doc.name} contains \n {my_doc.body}")

