from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Ledger
from .forms import AccountForm

from contacts.models import Contact
from communications.models import Cummunication
from communications.forms import CummunicationForm

# Create your views here.

@login_required(login_url='account_login')
def account_list(request):
    ledgers = Ledger.objects.all().order_by('created_on')
    paginator = Paginator(ledgers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    account_search = ledgers.filter(Q(name__icontains=q))

    context = {
        'ledgers': ledgers,
        'page_obj': page_obj,
        'account_search': account_search
    }
    return render(request, 'ledger/account_list.html', context)

@login_required(login_url='account_login')
def account_detail(request, pk):
    ledger = Ledger.objects.get(pk=pk)
    contacts = Contact.objects.filter(ledger=ledger)
    communications = Cummunication.objects.filter(
        ledger=ledger).order_by('-created_on')
    form = CummunicationForm
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
            return redirect('ledger:account_list')
    return render(request, 'ledger/account_cru.html', {'form': form})

@login_required(login_url='account_login')
def edit_account(request, pk):
    ledger = Ledger.objects.get(pk=pk)
    form = AccountForm(instance=ledger)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=ledger)
        if form.is_valid():
            form.save()
            return redirect('ledger:account_list')
    return render(request, 'ledger/account_cru.html', {'form': form})
   
