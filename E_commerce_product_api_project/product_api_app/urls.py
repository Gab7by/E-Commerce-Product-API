from django.urls import path
from . import views

urlpatterns = [
    path("user/register", views.RegisterView.as_view()),
    path("user/login", views.LoginView.as_view()),
    path("products", views.ApiProducts.as_view()),
    path("products/<str:pk>", views.ApiProduct.as_view())
]
  
