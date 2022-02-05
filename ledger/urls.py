from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('ledger/', views.account_list, name="ledger"),
    path('account_detail/<int:pk>/', views.account_detail, name="account-detail")
]
