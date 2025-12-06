from django.urls import path
from . import views

urlpatterns = [
    path("users", views.api_users),
    path("products", views.api_products)
]
  
