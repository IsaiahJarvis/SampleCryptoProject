from django.shortcuts import render, HttpResponse
from .models import TodoItem, Crypto
from .scripts import get_crypto_api

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def get_crypto(request):
    items = Crypto.objects.all().order_by('-market_cap')
    return render(request, "api_response.html", {"coins": items})