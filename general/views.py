# Create your views here.
from django.shortcuts import render


def index(request):
    # View code here...
    return render(request, 'splash.html')

def register(request):
    # View code here...
    return render(request, 'register.html')