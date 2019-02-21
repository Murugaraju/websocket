from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import asyncio
from websocket import create_connection
Tablename=[1,'empty']
# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=20)

    def save(self,*args,**kwargs):
        
        Tablename[0]=self.name
        ws = create_connection("ws://127.0.0.1:8000/channel/")
        ws.send(self.name)
        ws.close()
        return super().save(*args,**kwargs)

