from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Cummunication
from .forms import CummunicationForm

# Create your views here.

@login_required(login_url='account_login')
def comm_detail(request, pk):
    comm = Cummunication.objects.get(pk=pk)
    return render(request, 'communications/comm_detail.html', {'comm': comm})

@login_required(login_url='account_login')
def add_comm(request, ledger):
    form = CummunicationForm

    if request.method == 'POST':
        form = CummunicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'ledger:account-detail', 
                args=(ledger.uuid,)
            )
    return render(request, 'communications/comm_cru.html', {'form': form})

@login_required(login_url='account_login')
def edit_comm(request, pk, ledger):
    comm = Cummunication.objects.get(pk=pk)
    form = CummunicationForm(instance=comm)

    if request.method == 'POST':
        form = CummunicationForm(request.POST, instance=comm)
        if form.is_valid():
            form.save()
            return redirect(
                'ledger:account-detail', 
                args=(ledger.uuid,)
            )
    return render(request, 'communications/comm_cru.html', {'form': form})

@login_required(login_url='account_login')
def delete_comm(request, pk, ledger):
    comm = Cummunication.objects.get(pk=pk)

    if request.method == 'POST':
        comm.delete()
        return redirect(
            'ledger:account-detail', 
            args=(ledger.uuid,)
        )
    return render(request, 'delete_obj.html', {'obj': comm})