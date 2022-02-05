from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Ledger

# Create your views here.

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

def account_detail(request, pk):
    ledger = Ledger.objects.get(pk=pk)
    return render(request, 'ledger/account_detail.html', {'ledger': ledger})