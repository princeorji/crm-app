from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def communications(request):
    return HttpResponse('welcome')