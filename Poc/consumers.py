import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from Poc.models import Tablename

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Connected",event)
        await self.send({
            "type":"websocket.accept"
        })

        await self.send({
            "type": "websocket.send",
            "text":"Hello bro"
        })
        while 1:
            prev='radfasdf'
            
            if Tablename[0] !=1 and prev !=Tablename[0]:
                prev=Tablename[0]
                await self.send({
                "type": "websocket.send",
                "text":str(Tablename)
                })
                print(Tablename[0] !=1 and prev !=Tablename[0] )
                
            # if True:
            #     await self.send({
            #     "type": "websocket.send",
            #     "text":str(Tablename)
            #     })
            await asyncio.sleep(1)
            print("Table name =====>",Tablename)
            # await self.send({
            # "type": "websocket.send",
            # "text":"Tock"+str(Tablename[0])
            #     })
        

    async def websocket_receive(self,event):
        print("recieved ",event)
        await self.group_send({
             "type": "websocket.send",
            "text": "I am from backend your message is "+event['text']
        })

    async def websocket_disconnect(self, event):
        pass

class NosyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send("I am sending dude"
        )
        await self.channel_layer.group_add("gossip",self.channel_name)
        print(f"Added {self.channel_name} to gossip group")
    async def disconnect(self):
        
        
        await self.channel_layer.group_discard("gossip",self.channel_name)
        print(f"Removed {self.channel_name} to gossip group")
    async def sample_update(self,event):
        await self.send_json(event)
        print(f"Got message {event } at {self.channel_name}")