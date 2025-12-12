from django.urls import path
from . import views

urlpatterns = [
    path("users", views.ApiUsers.as_view()),
    path("products", views.ApiProducts.as_view()),
    path("products/<str:pk>", views.ApiProduct.as_view())
]
  
