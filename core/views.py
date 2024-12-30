from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view()

# Create your views here.
def shop(request):
    return Response('this is the shop')