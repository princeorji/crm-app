from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Ledger
from .forms import AccountForm

from contacts.models import Contact
from communications.models import Communication
from communications.forms import CommunicationForm

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AccountListView(ListView):
    paginate_by = 10
    template_name = 'ledger/account_list.html'
    context_object_name = 'ledgers'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            account_list = Ledger.objects.filter(
                name__icontains=q
            ).order_by('-created_on')
        else:
            account_list = Ledger.objects.all().order_by('-created_on')
        return account_list

@login_required(login_url='account_login')
def account_detail(request, uuid):
    ledger = Ledger.objects.get(pk=uuid)
    contacts = Contact.objects.filter(ledger=ledger)
    communications = Communication.objects.filter(
        ledger=ledger).order_by('-created_on')
    form = CommunicationForm
    context = {
        'ledger': ledger,
        'contacts': contacts,
        'communications': communications,
        'form': form,
    }
    return render(request, 'ledger/account_detail.html', context)

@login_required(login_url='account_login')
def add_account(request):
    form = AccountForm

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger:account-list')
    return render(request, 'ledger/account_cru.html', {'form': form})

@login_required(login_url='account_login')
def edit_account(request, uuid):
    ledger = Ledger.objects.get(pk=uuid)
    form = AccountForm(instance=ledger)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=ledger)
        if form.is_valid():
            form.save()
            return redirect('ledger:account-list')
    return render(request, 'ledger/account_cru.html', {'form': form})
   
