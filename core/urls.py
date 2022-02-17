from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.index, name="index"),
    path('create_customer/', views.create_customer, name="create-customer"),
    path('update_customer/<int:pk>/', views.update_customer, name="update-customer"),
    path('delete_customers/<int:pk>/', views.delete_customer, name="delete-customer"),
]
