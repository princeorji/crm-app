from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact_detail/<int:uuid>/', views.contact_detail, name="contact-detail"),
    path('add_contact/', views.add_contact, name="add-contact"),
    path('edit_contact/<int:uuid>/', views.edit_contact, name="edit-contact"),
    path('delete_contact/<int:uuid>/', views.delete_contact, name="delete-contact"),
]