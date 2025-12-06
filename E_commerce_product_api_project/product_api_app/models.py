from django.db import models 

class User(models.Model):
    username = models.CharField(max_length=300, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
    
class Product(models.Model):
    name = models.CharField(max_length=255, default= "Unkown product")
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    available_colours = models.JSONField(default=list, blank=True, null=True)
    available_sizes = models.JSONField(default=list, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return f"Product #{self.id}"
    

    

