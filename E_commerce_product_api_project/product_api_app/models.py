from django.db import models
import uuid 

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    product_name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    available_colours = models.JSONField(default=list, blank=True, null=True)
    available_sizes = models.JSONField(default=list, blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
    def __str__(self):
        return f"Product #{self.id}"
    
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, db_column='customer_id')
    order_date = models.DateTimeField(auto_now_add=True)
    
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id', related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    colour = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    
    @property
    def total_price(self):
        return self.quantity * self.unit_price
    
    class Meta:
        unique_together = ('order', 'product')
        
    def __str__(self):
        return f"{self.quantity} * {self.product.product_name}"

    

