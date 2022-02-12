from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.index, name="index"),
    path('create_client/', views.create_client, name="create-client"),
    path('update_client/<int:pk>/', views.update_client, name="update-client"),
    path('delete_client/<int:pk>/', views.delete_client, name="delete-client"),
]
