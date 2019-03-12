import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer,JsonWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class Chatchanell(AsyncConsumer):
    
    async def websocket_connect(self,event):
        print("Connected",event)
        self.chat_room='checking'
       

        await self.channel_layer.group_add(
            'checking',
            self.channel_name 
        )
        await self.send({
            "type":"websocket.accept"
        })
        await self.send({
            "type":"websocket.send",
            "text":"Websocket handshake done, channel connected"
        })
        



        

    async def websocket_receive(self,event):
        print("recieved ",event)
        channel_layer=get_channel_layer()
        await channel_layer.group_send('checking',{
            "type":"connectedSocket.notify",
            "text": "I am from backend your message is "+event['text']
        })
        # await self.send({
        #     "type":"websocket.send",
        #     "text":"I am from backend your message is "+event['text']
        # })
        

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def connectedSocket_notify(self, event):
        await self.send({
                'type': "websocket.send",
                "text":event['text']
            })

