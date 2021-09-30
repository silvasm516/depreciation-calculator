from django.urls import path
from .views import Footer7View, calculate, DEPView, doubledb, syd, straightline
from . import views

urlpatterns = [
    path( '', DEPView.as_view(), name= "index"),
    path('Footer7/', Footer7View.as_view(), name= 'Footer7'),
    path('Z', doubledb, name= 'doubledb'),
    path('X', syd, name= 'syd'),
    path('Y', straightline, name= 'straightline'),
    path('A', calculate, name= 'calculate'),

    
    
]