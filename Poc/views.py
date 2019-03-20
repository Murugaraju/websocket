from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.signals import post_save
from django.dispatch import receiver
from Poc.models import *
# Create your views here.

def test(request):
    return render(request,'index.html')


# class Testt(generics.CreateAPIView):
#     serializer_class=
#     def post(self):
#         return Response("I am working")
@api_view(['Get'])
def Testt(request):
    return Response("I am working")
@receiver(post_save,sender=Sample)
def dumma(sender,instance,created,**kwargs):
    print("I am printing created value da dubuku    ===>  ",created )