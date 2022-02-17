from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Customer
from .forms import CustomerForm

# Create your views here.

@login_required(login_url='account_login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='account_login')
def create_customer(request):
    form = CustomerForm

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    return render(request, 'customers/customer_cru.html', {'form': form})

@login_required(login_url='account_login')
def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    return render(request, 'customers/customer_cru.html', {'form': form})

@login_required(login_url='account_login')
def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        customer.delete()
        return HttpResponseRedirect(reverse('customer:index'))
    return render(request, 'delete_obj.html', {'obj': customer})


