from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('ledger/', views.account_list, name="ledger")
]
