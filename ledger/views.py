from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def AccountList(request):
    return HttpResponse("Account List")
