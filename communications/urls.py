from django.urls import path
from . import views

app_name = 'communications'

urlpatterns = [
    path('comm_detail/<int:pk>/', views.comm_detail, name="comm-detail"),
]