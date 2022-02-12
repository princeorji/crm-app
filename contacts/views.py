from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm

# Create your views here.

@login_required(login_url='account_login')
def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required(login_url='account_login')
def add_contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'contacts/contact_cru.html', {'form': form})

@login_required(login_url='account_login')
def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'contacts/contact_cru.html', {'form': form})

@login_required(login_url='account_login')
def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'delete_obj.html', {'obj': contact})
