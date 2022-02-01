from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Client
from .forms import ClientForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_client(request):
    form = ClientForm

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:index'))
    return render(request, 'core/create_client.html', {'form': form})

def update_client(request, pk):
    client = Client.objects.get(pk=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:index'))
    return render(request, 'core/update_client.html', {'form': form})

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)

    if request.method == 'POST':
            client.delete()
            return HttpResponseRedirect(reverse('core:index'))
    return render(request, 'core/delete_client.html', {'obj': client})


