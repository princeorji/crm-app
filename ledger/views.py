from lib2to3.pgen2.pgen import generate_grammar
import django
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Ledger

# Create your views here.

def account_list(request):
    ledgers = Ledger.objects.all()
    paginator = Paginator(ledgers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'ledgers': ledgers,
        'page_obj': page_obj
    }
    return render(request, 'ledger/account_list.html', context)
