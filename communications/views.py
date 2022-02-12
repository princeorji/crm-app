from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Cummunication

# Create your views here.

@login_required(login_url='account_login')
def comm_detail(request, pk):
    comm = Cummunication.objects.get(pk=pk)
    return render(request, 'comm_detail.html', {'comm': comm})