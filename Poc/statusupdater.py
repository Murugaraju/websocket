from Poc.model import Sample
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save,sender=Sample)
def announce_samplechange(sender,instance,created,**kwargs):
    if created:
        print("I am executed because change happened in Sample Model")
        # channel_layer=get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     "gossip",{"type":"sample.update",
        #     "event":"changes happend",
        #     "name":instance.name}
        # )