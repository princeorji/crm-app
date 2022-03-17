from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm

# Create your views here.

@login_required(login_url='account_login')
def contact_detail(request, uuid):
    contact = Contact.objects.get(pk=uuid)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required(login_url='account_login')
def add_contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    return render(request, 'contacts/contact_cru.html', {'form': form})

@login_required(login_url='account_login')
def edit_contact(request, uuid):
    contact = Contact.objects.get(pk=uuid)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect()
    return render(request, 'contacts/contact_cru.html', {'form': form})

@login_required(login_url='account_login')
def delete_contact(request, uuid):
    contact = Contact.objects.get(pk=uuid)

    if request.method == 'POST':
        contact.delete()
        return redirect()
    return render(request, 'delete_obj.html', {'obj': contact})
