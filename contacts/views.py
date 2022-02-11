from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def add_contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'contacts/cru_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'contacts/cru_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse('/success/'))
    return render(request, 'contacts/delete_contact.html', {'obj': contact})
