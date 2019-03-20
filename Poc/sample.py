from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['Get'])
def chann_working(request):
    async_to_sync(get_channel_layer().group_send)('checking',{
            "type":"connectedSocket.notify",
            "text": "I can send details from backend "
        })
    return Response("I am working") 
