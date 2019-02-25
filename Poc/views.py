from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
