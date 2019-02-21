from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
Tablename=[1,'empty']
# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=20)

    def save(self,*args,**kwargs):
        
        Tablename[0]=self.name
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('checking', {
            'type': 'connectedUser.notify',
            'text': 'triggered'
        })
        return super().save(*args,**kwargs)

