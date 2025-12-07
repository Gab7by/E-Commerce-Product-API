from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer
from .models import User, Product

@api_view(['POST'])
def api_users(request):
    serializer = UserSerializer(data=request.data)
    if serializer.Is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



