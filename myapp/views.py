from django.http import HttpResponse
from django.shortcuts import render


def data_view(request):
    return HttpResponse("Это страница DATA с определённым содержимым.")

def test_view(request):
    return HttpResponse("Это страница TEST с другим содержимым.")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
