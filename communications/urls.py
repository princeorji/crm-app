from django.urls import path
from . import views

app_name = 'communications'

urlpatterns = [
    path('comm_detail/<int:pk>/', views.comm_detail, name="comm-detail"),
    path('add_comm/', views.add_comm, name="add-comm"),
    path('edit_comm/<int:pk>/', views.edit_comm, name="edit-comm"),
    path('delete_comm/<int:pk>/', views.delete_comm, name="delete-comm"),
]