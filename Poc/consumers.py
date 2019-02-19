import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from chat.models import Tablename

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Connected dubuku",event)
        await self.send({
            "type":"websocket.accept"
        })

        await self.send({
            "type": "websocket.send",
            "text":"Hello bro"
        })
        for i in range(10):
            asyncio.sleep(3)

            await self.send({
                "type": "websocket.send",
                "text": "Hello bro"
            })

    async def websocket_recieve(self,event):
        pass

    async def websocket_disconnect(self, event):
        pass