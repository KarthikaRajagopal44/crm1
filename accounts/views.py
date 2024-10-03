from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Home')

def products(request):
    return HttpResponse('Products')

def customer(request):
    return HttpResponse('Customer')