from django.urls import path
from .views import data_view, test_view
from . import views

urlpatterns = [
    path('data/', data_view, name='data'),
    path('test/', test_view, name='test'),
]
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
