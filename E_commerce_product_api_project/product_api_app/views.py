from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer
from .models import User, Product
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView


class ApiUsers(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
    
class ApiProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     
class ApiProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





