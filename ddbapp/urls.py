from django.urls import path
from .views import DDBView, Footer7View, calculate
from . import views

urlpatterns = [
    path('index/', DDBView.as_view(), name='index'),
    path('Footer7/', Footer7View.as_view(), name= 'Footer7'),
    path('A', calculate, name= 'calculate'),
    
]