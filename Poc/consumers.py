import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer,JsonWebsocketConsumer
from channels.db import database_sync_to_async
from Poc.models import Tablename
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

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
        # while 1:
        #     asyncio.sleep(1)
        #     prev=Tablename[1]
        #     if Tablename[0] !=1 and prev !=Tablename[0]:
        #         print("First state",Tablename[0] !=1 and prev !=Tablename[0] )

        #         Tablename[1]=Tablename[0]
        #         await self.send({
        #         "type": "websocket.send",
        #         "text":str(Tablename)
        #         })
        #         print("second state",Tablename[0] !=1 and prev !=Tablename[0] )

                
            # if True:
            #     await self.send({
            #     "type": "websocket.send",
            #     "text":str(Tablename)
            #     })
            # await asyncio.sleep(1)
            # print("Table name =====>",Tablename)
            # await self.send({
            # "type": "websocket.send",
            # "text":"Tock"+str(Tablename[0])
            #     })
        

    async def websocket_receive(self,event):
        print("recieved ",event)
        await self.send({
             "type": "websocket.send",
            "text": "I am from backend your message is "+event['text']
        })

    async def websocket_disconnect(self, event):
        pass

class NosyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # await self.send("I am sending dude"
        # )
        # while 1:
        #     asyncio.sleep(1)
        #     prev=Tablename[1]
        #     if Tablename[0] !=1 and prev !=Tablename[0]:
        #         print("First state",Tablename[0] !=1 and prev !=Tablename[0] )

        #         Tablename[1]=Tablename[0]
        #         await self.send({
        #         "type": "websocket.send",
        #         "text":str(Tablename)
        #         })
        # #         print("second state",Tablename[0] !=1 and prev !=Tablename[0] )

    async def disconnect(self):
        
        
        await self.channel_layer.group_discard("gossip",self.channel_name)
        print(f"Removed {self.channel_name} to gossip group")
class Chatchanell(AsyncConsumer):
    
    async def websocket_connect(self,event):
        print("Connected",event)
        self.chat_room='checking'
        await self.send({
            "type":"websocket.accept"
        })

        await self.channel_layer.group_add(
            'checking',
            self.channel_name 
        )
        await self.send({
            "type":"websocket.send",
            "text":"hello"
        })
        



        

    async def websocket_receive(self,event):
        print("recieved ",event)
        channel_layer=get_channel_layer()
        # await channel_layer.group_send('checking',{
        #     "type":"websocket.send",
        #     "text": "I am from backend your message is "+event['text']
        # })
        await self.send({
            "type":"websocket.send",
            "text":"I am from backend your message is "+event['text']
        })
        

    async def websocket_disconnect(self, event):
        pass




class EventConsumer(JsonWebsocketConsumer):
    
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("Closed websocket with code: ", close_code)
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        self.close()

    def receive_json(self, content, **kwargs):
        print("Received event: {}".format(content))
        
        self.send_json({"text":"I am from backend"})
