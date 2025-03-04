from django.http import HttpResponse

def data_view(request):
    return HttpResponse("Это страница DATA с определённым содержимым.")

def test_view(request):
    return HttpResponse("Это страница TEST с другим содержимым.")
