from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact_detail/<int:pk>/', views.contact_detail, name="contact-detail"),
    path('add_contact/', views.add_contact, name="add-contact"),
    path('edit_contact/<int:pk>/', views.edit_contact, name="edit-contact"),
    path('delete_contact/<int:pk>/', views.delete_contact, name="delete-contact"),
]