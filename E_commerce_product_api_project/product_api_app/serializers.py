from rest_framework import serializers
from .models import User, Product, Customer, Order, OrderDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "description", "unit_price", "category", "available_colours", "available_sizes"]
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ["order", "product", "quantity", "unit_price", "colour", "size", "total_price"]
        
        
        