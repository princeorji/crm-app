from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('account_list/', views.account_list, name="account-list"),
    path('account_detail/<int:pk>/', views.account_detail, name="account-detail"),
    path('add_account/', views.add_account, name="add-account"),
]
