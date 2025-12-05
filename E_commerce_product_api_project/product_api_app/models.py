from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_lenght=200)
    
class Customer(models.Model):
    first_name = models.CharField(max_lenght=100)
    last_name = models.CharField(max_lenght=100)
    phone_number = models.CharField(max_lenght=20)
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    product_name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digit=10, decimal_places=2)
    category = models.CharField(max_length=200)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    available_colours = models.JSONField(default=list, blank=True, null=True)
    available_sizes = models.JSONField(default=list, blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id}"
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_details')
    
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    colour = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        unique_together = ('order', 'product')
        
    def __str__(self):
        return f"{self.quantity} * {self.product.product_name}"

    

